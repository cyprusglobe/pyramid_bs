from pyramid.httpexceptions import HTTPFound

from pyramid.security import (
    forget,
    NO_PERMISSION_REQUIRED,
)

from pyramid.view import (
    view_config,
    view_defaults,
)


@view_defaults(
    route_name='logout',
    permission=NO_PERMISSION_REQUIRED
)
class LogoutView(object):
    def __init__(self, request):
        self.request = request

    @view_config(request_method="GET")
    def get(self):
        self.request.session.invalidate()
        if self.request.userid:
            self.request.session.flash('Logout successful!')

        return HTTPFound(location=self.request.route_url('index'),
                         headers=forget(self.request))
