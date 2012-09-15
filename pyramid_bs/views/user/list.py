
import logging
import functools
import transaction

from pyramid.httpexceptions import HTTPFound

from pyramid.view import (
    view_config,
    view_defaults,
)

from sqlalchemy.exc import IntegrityError

from ...forms.user import (
    GroupForm,
)

from ...models.user import User
from ...models.user import Group
from ...utils import memoized

from ...models import DBSession
from pyramid.location import lineage

log = logging.getLogger(__name__)


@view_defaults(
    route_name='user_list',
    permission='basic',
)
class UserListView(object):
    def __init__(self, request):
        self.form = functools.partial(self._form)
        self.user = User.by_id(request.matchdict.get('user_id', 0))
        self.request = request

    @memoized
    def _form(self):
        request = self.request
        formdata = request.GET if request.is_xhr else request.POST
        lin = list(lineage(self.request.context))
        lin.reverse()
        print lin
        print request.resource_url(lin)
        return GroupForm(formdata, obj=self.user)

    @view_config(renderer='json', request_method="GET", xhr=True)
    def xhr(self):
        form = self.form()
        return form.json_errors(self.user)

    @view_config(renderer='/user/list.mako', request_method="GET")
    def get(self):
        return {
            'form': self.form(),
            'users': User.by_permission(u'secured'),
        }

    @view_config(renderer='/user/list.mako', request_method="POST")
    def post(self):
        form = self.form()
        response = None
        request = self.request
        print form.data
        print request
        search = form.data.get('group')
        print search
        print form.validate

        # redirect the user if needed
        if response:
            return response

        # redraw the page
        return self.get()
