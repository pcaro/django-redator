from django.conf.urls import url

from .forms import FileForm, ImageForm
from .views import upload, images_json

urlpatterns = [
    url('^upload/image/', upload, {'form_class': ImageForm}, name='upload-image'),
    url('^upload/file/', upload, {'form_class': FileForm}, name='upload-file'),
    url('^images.json', images_json, name='images-json'),
]
