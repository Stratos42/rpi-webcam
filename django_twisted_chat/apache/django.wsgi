import os, sys

sys.path.append('/home/france_a/aufrinfo.net/test/cgi/django_twisted_chat')

os.environ['DJANGO_SETTINGS_MODULE'] = 'django_twisted_chat.settings'

import django.core.handlers.wsgi

_application = django.core.handlers.wsgi.WSGIHandler()

def application(environ, start_response):
    environ['PATH_INFO'] = environ['PATH_INFO']
    return _application(environ, start_response)
