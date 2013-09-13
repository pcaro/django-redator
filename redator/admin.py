from django.contrib import admin
from django.db.models import TextField

from redactor.widgets import RedactorEditor


class RedactorModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        TextField: {'widget': RedactorEditor},
    }

    class Media:
        js = ('redactor/jquery-1.7.min.js',)
        css = {'all': ('redactor/css/django_admin.css',)}
