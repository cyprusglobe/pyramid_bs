import logging
import functools
from pyramid.view import (
    view_config,
    view_defaults,
)

from ...forms.user import (
    GroupForm,
)

from ...models.user import User
from ...utils import memoized

log = logging.getLogger(__name__)


@view_defaults(
    route_name='user_list',
    permission='basic',
)
class UserListView(object):
    def __init__(self, request):
        self.user = User.by_id(request.matchdict.get('user_id', 0))
        self.request = request


    @view_config(renderer='/user/list.mako', request_method="GET")
    def get(self):
        return {
        'users': User.by_permission(u'secured'),
        }

    @view_config(renderer='/user/list.mako', request_method="POST")
    def post(self):
        response = None
        request = self.request
        print form.data
        print request

        # redirect the user if needed
        if response:
            return response

        # redraw the page
        return self.get()
