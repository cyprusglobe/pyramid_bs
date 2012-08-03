from pyramid.httpexceptions import HTTPFound

from pyramid.view import (
    view_config,
    view_defaults,
)

from pyramid.security import NO_PERMISSION_REQUIRED

from login import LoginView


@view_defaults(
    route_name='index',
    permission=NO_PERMISSION_REQUIRED,
)
class IndexView(object):
    def __init__(self, request):
        self.request = request
        self.login = LoginView(request)

    @view_config(renderer='json', request_method="GET", xhr=True)
    def xhr(self):
        return self.login.xhr()

    @view_config(renderer='/index.mako', request_method="GET")
    def get(self):
        request = self.request
        if request.userid:
            return HTTPFound(location=request.route_url('user_list'))
        return {
            'form': self.login.form(),
        }

    @view_config(renderer='/index.mako', request_method="POST")
    def post(self):
        return self.login.post()
