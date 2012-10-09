import logging
from pyramid.view import (
    view_config,
    view_defaults,
)

from gravatar import Gravatar

from ...models.user import User

log = logging.getLogger(__name__)


@view_defaults(
    route_name='user_view',
    permission='basic',
)
class UserView(object):
    def __init__(self, request):
        self.request = request

    @view_config(renderer='/user/view.mako', request_method="GET")
    def get(self):
        gravatar = Gravatar('kjones@lobo.net', secure=True, size=50).thumb

        return {
            'gravatar': gravatar,
            'user': User.by_id(self.request.matchdict.get('user_id', 0)),
        }
