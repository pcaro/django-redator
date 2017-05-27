from django import forms

from . import models


class FileForm(forms.ModelForm):
    class Meta:
        model = models.File
        fields = '__all__'


class ImageForm(forms.ModelForm):
    class Meta:
        model = models.Image
        fields = '__all__'
