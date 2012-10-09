import unittest
import transaction

from pyramid import testing

from .models import DBSession


class TestMyView(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        from sqlalchemy import create_engine
        engine = create_engine('mysql+mysqldb://root@127.0.0.1:3306/pyramid_bs?charset=utf8')
        from .models import (
            Base)
        from .models.user import User
        from .models.user import Group
        DBSession.configure(bind=engine)
        Base.metadata.create_all(engine)
        with transaction.manager:
            # model = MyModel(name='one', value=55)
            # DBSession.add(model)
            user = User()
            group1 = Group()
            group1.name = u'secured'
            user.login = u'googless'
            user.password = u'test123'
            user.first_name = u'Google'
            user.last_name = u'Googles'
            user.phone = u'505-263-5626'
            user.email = u'sheldon@lobo.net'
            user.mygroups.append(group1)
            DBSession.add(user)
            DBSession.flush()

    def tearDown(self):
        DBSession.remove()
        testing.tearDown()

    def test_it(self):
        request = testing.DummyRequest()
        pass
