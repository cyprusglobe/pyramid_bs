import functools
import transaction

from pyramid.httpexceptions import HTTPFound

from pyramid.view import (
    view_config,
    view_defaults,
)

from sqlalchemy.exc import IntegrityError

from ...forms.user import (
    EditForm,
    AddForm,
)

from pyramid.security import Allow, Everyone

from ...models.user import User
from ...models.user import Group
from ...utils import memoized

from ...models import DBSession


@view_defaults(
    route_name='user_edit',
    permission='secured',
)
class UserEditView(object):
    @property
    def __acl__(self, userid):
        return [
            (Allow, self.request.userid, 'basic'),
        ]

    def __init__(self, request):
        self.form = functools.partial(self._form)
        self.user = User.by_id(request.matchdict.get('user_id', 0))
        self.request = request

    @memoized
    def _form(self):
        request = self.request
        formdata = request.GET if request.is_xhr else request.POST
        extra = {'secured': False, 'basic': False}
        try:
            if self.user:
                if self.user.mygroups:
                    for group in self.user.mygroups:
                        extra[group.name] = True
                return EditForm(formdata, obj=self.user, **extra)
            else:
                return AddForm(formdata, obj=self.user, **extra)
        except Exception, e:
            print e.message

    @view_config(renderer='json', request_method="GET", xhr=True)
    def xhr(self):
        form = self.form()
        return form.json_errors(self.user)

    @view_config(renderer='/user/edit.mako', request_method="GET")
    def get(self):
        return {
            'form': self.form(),
            'user': self.user,
        }

    @view_config(renderer='/user/edit.mako', request_method="POST")
    def post(self):
        form = self.form()
        response = None
        request = self.request

        savepoint = transaction.savepoint()
        # validate form data
        if form.validate(self.user):
            try:
                # update an existing user
                if self.user:
                    # don't change the passwod unless the user privides one
                    if form.data.get('password') == u'':
                        form.__delitem__('password')

                    form.populate_obj(self.user)
                    for groupname in [u'basic', u'secured']:
                        if form.data.get(groupname) is True:
                            # grant group permission
                            self.user.grant_group(groupname)
                        else:
                            # revoke group permission
                            self.user.revoke_group(groupname)

                    self.user.update()
                    request.session.flash('User updated successfully!')

                # add a new user
                else:
                    user = User()
                    form.populate_obj(user)
                    for groupname in [u'basic', u'secured']:
                        if form.data.get(groupname) is True:
                            group = Group()
                            group.name = groupname
                            user.mygroups.append(group)
                            user.add()
                        else:
                            user.add()
                            DBSession.flush()
                    request.session.flash('User added successfully!')

                # redirect the user back to the user list
                response = HTTPFound(location=request.route_url('user_list'))

            # login's are unique so catch any integrity errors
            except IntegrityError:
                savepoint.rollback()
                request.session.flash('Sorry that login exists!', 'error')

            # something went wrong
            except Exception, e:
                savepoint.rollback()
                request.session.flash('Error!', 'error')
                print e.message

        # redirect the user if needed
        if response:
            return response

        # redraw the page
        return self.get()
