from django.forms import widgets
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse
from django.utils import simplejson as json
from django.conf import settings


OPTIONS = getattr(settings, 'REDACTOR_OPTIONS', {})

INIT_JS = """<script type="text/javascript">
  jQuery(document).ready(function(){
    $("#%s").redactor(%s);
  });
</script>
"""


class RedactorEditor(widgets.Textarea):

    class Media:
        js = ('redactor/redactor.min.js',)
        css = {'all': ('redactor/css/redactor.css',)}

    def __init__(self, *args, **kwargs):
        super(RedactorEditor, self).__init__(*args, **kwargs)
        self.upload_to = kwargs.pop('upload_to', '')
        self.options = OPTIONS.copy()
        self.options.update(kwargs.pop('redactor_options', {}))
        self.options.update({
            'imageUpload': reverse('redactor_upload_image', kwargs={'upload_to': self.upload_to}),
            'fileUpload': reverse('redactor_upload_file', kwargs={'upload_to': self.upload_to})
        })

    def render(self, name, value, attrs=None):
        html = super(RedactorEditor, self).render(name, value, attrs)
        final_attrs = self.build_attrs(attrs)
        id_ = final_attrs.get('id')
        options = json.dumps(self.options)
        html += INIT_JS % (id_, options)
        return mark_safe(html)


# For backward compatibility
JQueryEditor = RedactorEditor
