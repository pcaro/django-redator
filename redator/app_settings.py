from django.conf import settings


UPLOAD_TO = getattr(settings, 'REDATOR_UPLOAD_TO', 'redator/%Y-%m/')
REDACTOR_OPTIONS = getattr(settings, 'REDATOR_REDACTOR_OPTIONS', {
    'autoresize': False,
    'cleanup': True,
    'lang': 'en',
    'wym': True,
})
