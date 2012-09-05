from pyramid.view import (
    view_config,
    view_defaults,
)


from ...models.user import User


@view_defaults(
    route_name='admin_list',
    permission='basic',
)
class AdminListView(object):
    def __init__(self, request):
        self.request = request

    @view_config(renderer='/admin/list.mako', request_method="GET")
    def get(self):
        return {
            'users': User.get_all(),
        }
