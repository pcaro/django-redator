import json

from PIL import Image, ImageOps
from StringIO import StringIO
from os import path

from django.contrib.auth.decorators import user_passes_test
from django.core.files.base import ContentFile
from django.http import HttpResponse
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET

from . import forms, models


@csrf_exempt
@require_POST
@user_passes_test(lambda u: u.is_staff)
def upload(request, upload_to, form_class=forms.ImageForm):
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
        return HttpResponse(json.dumps({
            'filelink': upload.file.url,
            'filename': upload.title
        }))
    return HttpResponse(status=403)


@require_GET
@user_passes_test(lambda u: u.is_staff)
def images_json(request):
    data = json.dumps([i.data for i in models.Image.objects.all()])
    return HttpResponse(data)
