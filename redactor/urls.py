from django.conf.urls.defaults import *
from redactor.views import redactor_upload

urlpatterns = patterns('',
    url('^upload/(?P<upload_to>.*)', redactor_upload, name='redactor_upload'),
)
