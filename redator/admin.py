from django.contrib import admin
from django.db.models import TextField

from .widgets import RedactorEditorAdmin


class RedactorAdmin(admin.ModelAdmin):
    formfield_overrides = {
        TextField: {'widget': RedactorEditorAdmin(
            attrs={'rows': 40}
        )},
    }
