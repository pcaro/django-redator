import json

from django.conf import settings
from django.core.urlresolvers import reverse
from django.forms import widgets
from django.utils.safestring import mark_safe

from . import app_settings


class RedactorEditor(widgets.Textarea):
    LANG_JS = '<script src="%sredactor/langs/%s.js"></script>'
    INIT_JS = ('<script type="text/javascript">jQuery(document).ready('
               'function(){jQuery("#%s").redactor(%s)}'
               ');</script>')

    class Media:
        if settings.DEBUG:
            js = ('redactor/redactor.js',)
        else:
            js = ('redactor/redactor.min.js',)
        css = {'all': ('redactor/redactor.css',)}

    def __init__(self, *args, **kwargs):
        self.widget_options = kwargs.pop('redactor_options', {})
        super(RedactorEditor, self).__init__(*args, **kwargs)

    @property
    def options(self):
        options = app_settings.REDACTOR_OPTIONS
        options.update(self.widget_options)
        options.update({
            'fileUpload': reverse('redator:upload-file'),
            'imageUpload': reverse('redator:upload-image'),
            'imageGetJson': reverse('redator:images-json'),
        })
        return options

    @property
    def language(self):
        return self.options.get('lang', 'en')

    def build_lang_js(self):
        if self.language != 'en':
            return self.LANG_JS % (settings.STATIC_URL, self.language)
        return ''

    def build_init_js(self, html_id):
        options = json.dumps(self.options)
        return self.INIT_JS % (html_id, options)

    def render(self, name, value, attrs=None):
        html = super(RedactorEditor, self).render(name, value, attrs)
        html_id = self.build_attrs(attrs).get('id')
        html += self.build_lang_js() + self.build_init_js(html_id)
        return mark_safe(html)


class RedactorEditorAdmin(RedactorEditor):
    class Media:
        css = {'all': ('admin/redator.css',)}
