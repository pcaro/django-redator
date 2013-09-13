from django.contrib import admin
from django.db.models import TextField

from .widgets import RedactorEditor


class RedactorModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        TextField: {'widget': RedactorEditor},
    }

    class Media:
        css = {'all': ('admin/redator.css',)}
