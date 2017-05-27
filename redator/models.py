from os import path

from django.db import models
from django.utils import dateformat

from . import app_settings


class Upload(models.Model):
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ('-date',)

    def __unicode__(self):
        return unicode(self.file.url)

    @property
    def title(self):
        return path.basename(self.file.name)

    @property
    def folder(self):
        return dateformat.format(self.date, 'F, Y')


class File(Upload):
    file = models.FileField('file', upload_to=app_settings.UPLOAD_TO)


class Image(Upload):
    file = models.ImageField('image', upload_to=app_settings.UPLOAD_TO)
    thumbnail = models.ImageField(
        'thumbnail',
        upload_to=app_settings.UPLOAD_TO,
        blank=True
    )

    @property
    def data(self):
        return {
            'thumb': self.thumbnail.url,
            'image': self.file.url,
            'title': self.title,
            'folder': self.folder,
        }
