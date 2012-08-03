import os
import sys
import transaction

from pyramid.config import Configurator

from pyramid.paster import (
    get_appsettings,
    setup_logging,
)

from sqlalchemy import engine_from_config

from ..models import (
    DBSession,
    Base,
)

from ..models.user import User
from ..models.user import Group


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri>\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) != 2:
        usage(argv)
    config_uri = argv[1]
    setup_logging(config_uri)
    settings = get_appsettings(config_uri)
    config = Configurator(settings=settings)
    config.scan('..models')
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)
    with transaction.manager:
        user = User()
        group1 = Group()
        group1.name = u'secured'
        user.login = u'sheldon'
        user.password = u'test123'
        user.first_name = u'Sheldon'
        user.last_name = u'Jones'
        user.phone = u'505-263-5626'
        user.email = u'sheldon@lobo.net'
        user.mygroups.append(group1)
        DBSession.add(user)
        DBSession.flush()
