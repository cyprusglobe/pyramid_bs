import functools

from pyramid.httpexceptions import HTTPFound
from pyramid.security import NO_PERMISSION_REQUIRED
from pyramid.security import remember

from pyramid.view import (
    view_config,
    view_defaults,
)

from ..forms.login import LoginForm
from ..models.user import User

from ..utils import memoized


@view_defaults(
    route_name='login',
    permission=NO_PERMISSION_REQUIRED
)
class LoginView(object):
    def __init__(self, request):
        self.request = request
        self.form = functools.partial(self._form)

    @memoized
    def _form(self):
        request = self.request
        formdata = request.GET if request.is_xhr else request.POST
        return LoginForm(formdata)

    @view_config(renderer='json', request_method="GET", xhr=True)
    def xhr(self):
        form = self.form()
        return form.json_errors()

    @view_config(renderer='/login.mako', request_method="GET")
    def get(self):
        request = self.request
        if request.userid:
            return HTTPFound(location=request.route_url('user_list'))
        return {
            'form': self.form(),
        }

    @view_config(renderer='/login.mako', request_method="POST")
    def post(self):
        form = self.form()
        request = self.request
        if form.validate():
            login = form.data.get('login')
            password = form.data.get('password')
            if User.check_password(login, password):
                request.session.flash('Welcome back!')
                referrer = self.request.GET.get('referrer')
                location = referrer or request.route_url('user_list')
                return HTTPFound(location=location,
                                 headers=remember(request, login))
            else:
                request.session.flash('Authentication Failed!', 'error')
        return self.get()
