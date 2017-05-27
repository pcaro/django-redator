import json

from django.conf import settings
from django.core.urlresolvers import reverse
from django.forms import widgets
from django.forms import Media
from django.utils.safestring import mark_safe

from . import app_settings


class RedactorEditor(widgets.Textarea):

    INIT_JS = ('<script type="text/javascript">jQuery(document).ready('
               'function(){jQuery("#%s").redactor(%s)}'
               ');</script>')

    def __init__(self, *args, **kwargs):
        self.widget_options = kwargs.pop('redactor_options', {})
        super(RedactorEditor, self).__init__(*args, **kwargs)

    def get_resources(self):
        if settings.DEBUG:
            js = ('redactor/redactor.js',)
        else:
            js = ('redactor/redactor.min.js',)
        if self.language != 'en':
            js += ('redactor/langs/%s.js' % self.language, )
        js += ('suit_admin_setup.js',)
        css = {
            'screen': [
                'redactor/redactor.css',
            ]
        }
        return js, css

    @property
    def media(self):
        js, css = self.get_resources()
        return Media(css=css, js=js)

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

    def build_init_js(self, html_id):
        options = json.dumps(self.options)
        return self.INIT_JS % (html_id, options)

    @property
    def language(self):
        return self.options.get('lang', 'en')

    def render(self, name, value, attrs=None):
        html = super(RedactorEditor, self).render(name, value, attrs)
        html_id = self.build_attrs(attrs).get('id')
        html += self.build_init_js(html_id)
        return mark_safe(html)


class RedactorEditorAdmin(RedactorEditor):

    @property
    def media(self):
        js, css = self.get_resources()
        css['screen'].append('css/redactor_admin.css')
        return Media(css=css, js=js)
