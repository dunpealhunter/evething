import os
import sys

sys.path.append('/home/freddie/git')
os.environ['DJANGO_SETTINGS_MODULE'] = 'everdi.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
