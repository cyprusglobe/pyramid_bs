import logging
from pyramid.view import (
    view_config,
    view_defaults,
)

from gravatar import Gravatar

from ...models.user import User

from pyramid.security import Allow, authenticated_userid, Everyone

log = logging.getLogger(__name__)


@view_defaults(
    route_name='user_list',
    permission='basic',
)
class UserListView(object):
    @property
    def __acl__(self, userid):
        return [
            (Allow, 'sheldon1' 'basic'),
        ]
    def __init__(self, request):
        self.user = User.by_id(request.matchdict.get('user_id', 0))
        self.request = request

    @view_config(renderer='/user/list.mako', request_method="GET")
    def get(self):

        return {
            # 'users': User.by_permission(u'secured'),
            'users': User.get_all(),
        }

    @view_config(renderer='/user/list.mako', request_method="POST")
    def post(self):
        response = None
        request = self.request
        print request

        # redirect the user if needed
        if response:
            return response

        # redraw the page
        return self.get()
