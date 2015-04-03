from ladon.server.wsgi import LadonWSGIApplication
from django.http.response import HttpResponse, HttpResponseServerError
from django.http.cookie import SimpleCookie
from django.apps import apps
import importlib
import os


def get_ladon_application():
    """
    Configure Ladon wsgi application,
    autodiscover ladon modules and paths
    """

    service_modules = []
    paths = []
    for app_config in apps.get_app_configs():
        # add webservices from ladon modules.
        module_name = '{}.ladon'.format(app_config.name)
        module_path = os.path.join(app_config.path, 'ladon.py')
        if os.path.exists(module_path):
            service_modules.append(module_name)

        # add ladon template paths
        template_path = os.path.join(app_config.path, 'templates/ladon')
        if os.path.exists(template_path):
            paths.append(template_path)

        # add ladon css paths
        css_path = os.path.join(app_config.path, 'static/ladon/css')
        if os.path.exists(css_path):
            paths.append(css_path)

    return LadonWSGIApplication(service_modules, paths)


def reraise(exc_info):
    """
    reraise exception so Django can handle it.
    """

    _etype, exc, tb = exc_info
    if exc.__traceback__ is not tb:
        raise exc.with_traceback(tb)
    raise exc


def fix_path(environ, path):
    """
    Move the part of the path consumed by the current view, from the PATH_INTO to the SCRIPT_NAME
    """

    if not environ['PATH_INFO'].endswith(path):
        raise HttpResponseServerError("Path %s is not the last part of the PATH_INFO in the "
                                      "original request (%s)" % (path, environ['PATH_INFO']))

    consumed_path = environ['PATH_INFO'][:-len(path)]
    environ['PATH_INFO'] = path
    environ['SCRIPT_NAME'] += consumed_path

LADON_APP = get_ladon_application()

# inspired by twod.wsgi - twod/wsgi/embedded_wsgi.py:call_wsgi_app and
# webob - webob/request.py:call_application
def ladon_view(request, path):
    """
    delegates request-handling to ladon's wsgi application
    """

    captured = []
    output = []

    def start_response(status, headers, exc_info=None):
        if exc_info is not None:
           reraise(exc_info)
        captured[:] = [status.split(' ', 1)[0], headers]
        return output.append

    environ = request.environ.copy()
    fix_path(environ, path)

    app_iter = LADON_APP(environ, start_response)
    if output or not captured:
        try:
            output.extend(app_iter)
        finally:
            if hasattr(app_iter, 'close'):
                app_iter.close()
        app_iter = output

    headers = captured[1]
    django_response = HttpResponse(app_iter, status=int(captured[0]))

    cookies = SimpleCookie()
    for (header, value) in headers:
        if header.upper() == "SET-COOKIE":
           cookies.load(value)
        else:
           django_response[header] = value

    django_response.cookies.update(cookies)
    return django_response
