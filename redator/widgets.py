import json

from django.conf import settings
from django.core.urlresolvers import reverse
from django.forms import widgets
from django.utils.safestring import mark_safe


PROJECT_OPTIONS = getattr(settings, 'REDATOR_REDACTOR_OPTIONS', {})

INIT_JS = """<script type="text/javascript">
  jQuery(document).ready(function(){
    $("#%s").redactor(%s);
  });
</script>
"""


class RedactorEditor(widgets.Textarea):
   
    def __init__(self, *args, **kwargs):
        super(RedactorEditor, self).__init__(*args, **kwargs)
        self.upload_to = kwargs.pop('upload_to', '')
        self.widget_options = kwargs.pop('redactor_options', {})

    def get_options(self):
        options = PRJECT_OPTIONS.copy()
        options.update(self.widget_options)
        options.update({
            'imageUpload': reverse('redactor_upload_image', kwargs={'upload_to': self.upload_to}),
            'fileUpload': reverse('redactor_upload_file', kwargs={'upload_to': self.upload_to})
        })
        return json.dumps(options)

    def render(self, name, value, attrs=None):
        html = super(RedactorEditor, self).render(name, value, attrs)
        final_attrs = self.build_attrs(attrs)
        id_ = final_attrs.get('id')
        html += INIT_JS % (id_, self.get_options())
        return mark_safe(html)

    def _media(self):
        return forms.Media(
            js=('redactor/redactor.min.js',)
            css={'all': ('redactor/css/redactor.css',)}
        )
    media = property(_media)


class RedactorEditorAdmin(RedactorEditor):
    def _media(self):
        media = super(RedactorEditorAdmin, self)._media()
        media.add_css({'all': ('admin/redator.css',)})
        return media
