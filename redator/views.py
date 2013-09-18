import json

from PIL import Image, ImageOps
from StringIO import StringIO
from os import path

from django import http
from django.contrib.auth.decorators import user_passes_test
from django.core.files.base import ContentFile
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET

from . import forms, models


@require_POST
@csrf_exempt
@user_passes_test(lambda u: u.is_staff)
def upload(request, form_class):
    form = form_class(request.POST, request.FILES)
    if form.is_valid():
        upload = form.save(commit=False)
        if form_class == forms.ImageForm:
            image = Image.open(upload.file.file)
            image_name = upload.file.name
            thumb = ImageOps.fit(image, (100, 100), Image.ANTIALIAS)
            thumb_name = path.splitext(image_name)[0] + 'thumb.jpg'
            buffer_ = StringIO()
            thumb.save(buffer_, format='JPEG')
            upload.thumbnail.save(thumb_name, ContentFile(buffer_.getvalue()))
        upload = form.save()
        return http.HttpResponse(json.dumps({
            'filelink': upload.file.url,
            'filename': upload.title
        }))
    return http.HttpResponseForbidden()


@require_GET
@user_passes_test(lambda u: u.is_staff)
def images_json(request):
    data = json.dumps([i.data for i in models.Image.objects.all()])
    return http.HttpResponse(data)
