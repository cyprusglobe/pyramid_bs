import transaction

from pyramid.httpexceptions import HTTPFound

from pyramid.security import Authenticated

from pyramid.view import (
    view_config,
    view_defaults,
)

from ...models.user import User


@view_defaults(
    route_name='user_delete',
    permission='secured',
)
class UserDeleteView(object):
    def __init__(self, request):
        self.request = request
        self.user = User.by_id(request.matchdict.get('user_id'))

    @view_config(request_method="GET")
    def get(self):
        request = self.request

        if not self.user:
            request.session.flash('Error loading user record!', 'error')
            return HTTPFound(location=request.route_url('user_list'))

        savepoint = transaction.savepoint()
        try:
            self.user.delete()
            request.session.flash('User deleted successfully!')

        except Exception, e:
            savepoint.rollback()
            request.session.flash('Error!', 'error')
            print e.message

        return HTTPFound(location=request.route_url('user_list'))
