from django.contrib import admin
from django.db import models

from .widgets import RedactorEditorAdmin


class RedactorAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': RedactorEditorAdmin(
            attrs={'rows': 24}
        )},
    }
