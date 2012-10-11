import cryptacular.bcrypt

from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    Unicode,
    ForeignKey,
)

from sqlalchemy.orm import synonym
from sqlalchemy.orm import relationship

from . import (
    Base,
    DBSession
)

from gravatar import Gravatar


crypt = cryptacular.bcrypt.BCRYPTPasswordManager()


def groupfinder(userid, request):
    user = User.by_login(userid)
    if user:
        return [('%s' % group.name) for group in user.mygroups]


class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(30))
    user_id = Column(Integer, ForeignKey('user.id'))

    @classmethod
    def by_name(cls, name):
        return DBSession.query(cls).filter(cls.name == name).first()

    def __repr__(self):
        return "<Group: %s>" % (self.name)


class User(Base):
    """
    User model.
    """
    __tablename__ = 'user'
    __table_args__ = {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'}
    id = Column(Integer, primary_key=True)
    login = Column(Unicode(100), unique=True)
    first_name = Column(Unicode(100))
    last_name = Column(Unicode(100))
    phone = Column(Unicode(100))
    email = Column(Unicode(100))
    mygroups = relationship(Group, backref='users')

    _password = Column('password', Unicode(100))

    def _get_password(self):
        return self._password

    def _set_password(self, password):
        self._password = self._hash_password(password)

    password = property(_get_password, _set_password)
    password = synonym('_password', descriptor=password)

    def __repr__(self):
        return "<User %s>" % (self.login)

    def _hash_password(self, password):
        return unicode(crypt.encode(password))

    @classmethod
    def by_permission(cls, permission):
        return DBSession.query(cls).join(Group).filter(Group.name == permission).all()

    @classmethod
    def by_id(cls, id):
        return DBSession.query(cls).filter(cls.id == id).first()

    @classmethod
    def by_login(cls, login):
        return DBSession.query(cls).filter(cls.login == login).first()

    @classmethod
    def get_all(cls, query_only=False):
        if query_only:
            return DBSession.query(cls).order_by(cls.login)
        return DBSession.query(cls).order_by(cls.login).all()

    @classmethod
    def gravatar(cls, email):
        gravatar = Gravatar(email, secure=True, size=50).thumb
        return gravatar

    @classmethod
    def check_password(cls, login, password):
        user = cls.by_login(login)
        if not user:
            return False
        return crypt.check(user.password, password)

    def add(self):
        try:
            DBSession.add(self)
            DBSession.flush()
        except Exception:
            raise

    def delete(self):
        try:
            DBSession.delete(self)
            DBSession.flush()
        except Exception:
            raise

    def change_password(self, password):
        try:
            self.password = password
            self.timestamp = datetime.now()
            DBSession.flush()

        except Exception:
            raise

    def update(self):
        try:
            DBSession.flush()
        except Exception:
            raise

    def has_group_name(self, group_name):
        for g in self.mygroups:
            if g.name == group_name:
                return True
        return False

    def grant_group(self, group_name):
        if not self.has_group_name(group_name):
            try:
                g = Group()
                g.name = group_name
                self.mygroups.append(g)
                DBSession.flush()
            except:
                raise

    def revoke_group(self, group_name):
        try:
            for g in self.mygroups:
                if g.name == group_name:
                    DBSession.delete(g)
                    DBSession.flush()
        except:
            raise
