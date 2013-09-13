from os.path import join
from django.conf import settings
from django.contrib.auth.decorators import user_passes_test
from django.core.files.storage import default_storage
from django.http import HttpResponse
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .forms import ImageForm


@csrf_exempt
@require_POST
@user_passes_test(lambda u: u.is_staff)
def redactor_upload(request, upload_to, form_class=ImageForm, response=lambda name, url: url):
    form = form_class(request.POST, request.FILES)
    if form.is_valid():
        file_ = form.cleaned_data['file']
        folder = now().strftime('%Y-%m')
        path = join(upload_to, folder, file_.name)
        real_path = default_storage.save(path, file_)
        return HttpResponse(
            response(file_.name, join(settings.MEDIA_URL, real_path))
        )
    return HttpResponse(status=403)
