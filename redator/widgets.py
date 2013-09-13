import json

from django.conf import settings
from django.core.urlresolvers import reverse
from django.forms import widgets
from django.utils.safestring import mark_safe


class RedactorEditor(widgets.Textarea):
    init_js = (
        '<script type="text/javascript">'
        'jQuery(document).ready(function(){jQuery("#%s").redactor(%s);});'
        '</script>'
    )

    class Media:
        js = ('redactor/redactor.min.js',)
        css = {'all': ('redactor/redactor.css',)}

    def __init__(self, *args, **kwargs):
        super(RedactorEditor, self).__init__(*args, **kwargs)
        self.upload_to = kwargs.pop('upload_to', '')
        self.widget_options = kwargs.pop('redactor_options', {})

    def get_options(self):
        options = getattr(settings, 'REDATOR_REDACTOR_OPTIONS', {})
        options.update(self.widget_options)
        options.update({
            'imageUpload': reverse(
                'redator:upload-image',
                kwargs={'upload_to': self.upload_to}
            ),
            'fileUpload': reverse(
                'redator:upload-file',
                kwargs={'upload_to': self.upload_to}
            )
        })
        return json.dumps(options)

    def render(self, name, value, attrs=None):
        html = super(RedactorEditor, self).render(name, value, attrs)
        final_attrs = self.build_attrs(attrs)
        id_ = final_attrs.get('id')
        html += self.init_js % (id_, self.get_options())
        return mark_safe(html)


class RedactorEditorAdmin(RedactorEditor):
    class Media:
        css = {'all': ('admin/redator.css',)}
