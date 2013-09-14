from django import forms

from . import models


class FileForm(forms.ModelForm):
    class Meta:
        model = models.File


class ImageForm(forms.ModelForm):
    class Meta:
        model = models.Image
