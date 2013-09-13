import json

from django.conf.urls.defaults import url, patterns

from .views import redactor_upload
from .forms import FileForm, ImageForm


urlpatterns = patterns('',
    url('^upload/image/(?P<upload_to>.*)', redactor_upload, {
        'form_class': ImageForm,
        'response': lambda name, url: json.dumps({'filelink': url}),
    }, name='upload-image'),

    url('^upload/file/(?P<upload_to>.*)', redactor_upload, {
        'form_class': FileForm,
        'response': lambda name, url: json.dumps({'filelink': url, 'filename': name}),
    }, name='upload-file'),
)
