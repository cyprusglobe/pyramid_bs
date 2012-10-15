from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.config import Configurator
from pyramid.httpexceptions import HTTPForbidden
from pyramid.security import DENY_ALL
from pyramid.security import NO_PERMISSION_REQUIRED
from pyramid.session import UnencryptedCookieSessionFactoryConfig
from pyramid_beaker import session_factory_from_settings

from sqlalchemy import engine_from_config

from .models import (
    DBSession,
    UserFactory,
    RootFactory,
)
from .models.user import groupfinder


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, prefix='sqlalchemy.')
    DBSession.configure(bind=engine)

    # my_session_factory = UnencryptedCookieSessionFactoryConfig('itsaseekreet')

    authentication_policy = AuthTktAuthenticationPolicy('seekrit',
                                                        callback=groupfinder)
    authorization_policy = ACLAuthorizationPolicy()

    session_factory = session_factory_from_settings(settings)
    config = Configurator(
        root_factory=RootFactory,
        settings=settings
    )
    config.set_session_factory(session_factory)

    config.set_default_permission(DENY_ALL)
    config.set_authentication_policy(authentication_policy)
    config.set_authorization_policy(authorization_policy)

    # redirect all HTTPForbidden requests to the forbidden view
    config.add_view('.views.forbidden',
                    context=HTTPForbidden,
                    permission=NO_PERMISSION_REQUIRED)

    config.add_static_view('static', 'static', cache_max_age=3600)

    config.add_route('request', '/request')

    config.add_route('index', '/')
    config.add_route('login', '/login')  # change obscure to hide login
    config.add_route('logout', '/logout')

    config.add_route('user_list', '/users', factory=UserFactory)
    config.add_route('user_view', '/user/{user_id}', factory=UserFactory, traverse='/{user_id}')
    config.add_route('user_edit', '/user/edit/{user_id}', factory=UserFactory, traverse='/{user_id}')
    config.add_route('user_delete', '/user/{user_id}/delete', factory=UserFactory, traverse='/{user_id}')

    config.scan()
    return config.make_wsgi_app()
