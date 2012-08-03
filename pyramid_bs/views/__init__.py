from pyramid.httpexceptions import HTTPForbidden
from pyramid.httpexceptions import HTTPFound
from pyramid.security import authenticated_userid


def forbidden(request):
    # do not allow a user to login if they are already logged in
    if authenticated_userid(request):
        request.session.flash('You cannot edit users your lacking Secured Permissions Your Currently only have Basic Permissions', 'error')
        location = request.route_url('index')
        #return HTTPForbidden()
    else:
        location = request.route_url('index', _query=(('referrer', request.path),))
    return HTTPFound(location=location)
