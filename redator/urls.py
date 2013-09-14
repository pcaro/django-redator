from django.conf.urls import url, patterns

from .forms import FileForm, ImageForm


urlpatterns = patterns(
    'redator.views',
    url('^upload/image/(?P<upload_to>.*)', 'upload', {'form_class': ImageForm}, name='upload-image'),
    url('^upload/file/(?P<upload_to>.*)', 'upload', {'form_class': FileForm}, name='upload-file'),
    url('^images.json', 'images_json', name='images-json'),
)
