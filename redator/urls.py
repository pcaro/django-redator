from django.conf.urls import url

from .forms import FileForm, ImageForm


urlpatterns = [
    url('^upload/image/', 'redator.views.upload', {'form_class': ImageForm}, name='upload-image'),
    url('^upload/file/', 'redator.views.upload', {'form_class': FileForm}, name='upload-file'),
    url('^images.json', 'redator.views.images_json', name='images-json'),
]
