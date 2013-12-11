import os, sys

sys.path.append('/home/france_a/aufrinfo.net/camera')

os.environ['DJANGO_SETTINGS_MODULE'] = 'picam_website.settings'

import django.core.handlers.wsgi

_application = django.core.handlers.wsgi.WSGIHandler()

def application(environ, start_response):
    environ['PATH_INFO'] = environ['PATH_INFO']
    return _application(environ, start_response)
