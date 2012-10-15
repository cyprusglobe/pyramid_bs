from pyramid.security import (
    Allow,
    Everyone,
    ALL_PERMISSIONS,
    authenticated_userid,
)

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
)

from pyramid.security import Authenticated

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(autocommit=False, autoflush=False,
                                        extension=ZopeTransactionExtension()))
Base = declarative_base()

from user import User


class RootFactory(object):
    __acl__ = [
        # (Allow, Everyone, 'everybody'),
        # (Allow, 'basic', 'basic'),
        (Allow, 'secured', ALL_PERMISSIONS),
    ]

    def __init__(self, request):
        self.request = request


class UserFactory(object):
    __acl__ = [
        (Allow, 'secured', ALL_PERMISSIONS),
    ]


    def __init__(self, request):
        self.request = request

    def __getitem__(self, key):
        user = User.by_id(key)
        user.__parent__ = self
        user.__name__ = key
        return user
