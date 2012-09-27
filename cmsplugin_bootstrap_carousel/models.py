from django.conf import settings
from os.path import dirname
if 'filer' in settings.INSTALLED_APPS:
    execfile(dirname(__file__)+"/models_filer.py")
else:
    execfile(dirname(__file__)+"/models_default.py")
