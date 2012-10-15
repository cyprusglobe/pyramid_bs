import logging
from pyramid.view import (
    view_config,
    view_defaults,
)

from pyramid.security import (
    Allow,
    Everyone,
)
from ...models.user import User

log = logging.getLogger(__name__)


@view_defaults(
    route_name='user_view',
    permission='basic',
)
class UserView(object):
    @property
    def __acl__(self):
        return [
            (Allow, Everyone, 'basic'),
        ]
    def __init__(self, request):
        self.request = request

    @view_config(renderer='/user/view.mako', request_method="GET")
    def get(self):
        return {
            'user': User.by_id(self.request.matchdict.get('user_id', 0)),
        }
