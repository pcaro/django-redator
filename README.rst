==============
Django Redator
==============

**Django Redator** (sic) is a application for the `Django Web
Framework`_ to help you integrate `Redactor`_, a beautiful and
easy-to-use WYSIWYG HTML editor, into your projects.

.. _`Django Web Framework`: http://www.djangoproject.com
.. _`Redactor`: http://imperavi.com/redactor/


Installing & Setup
==================

Redator is available on `Python Package Index (PyPI)`_ so you can
easily install the latest stable version of it using *pip*::

  pip instal django-redator

Using it together your Django forms is easy as using a custom
``CharField`` widget::

  from django import forms
  from redator.widgets import RedactorEditor

  class PostForm(forms.Form):
      title = forms.CharField()
      body = forms.CharField(widget=RedactorEditor)

Remember to render the media assets in your HTML template::

  {{ form.media }}
  {{ form }}

You can find more information about Django forms at
https://docs.djangoproject.com/en/dev/ref/forms/.

.. _`Python Package Index (PyPI)`: http://pypi.python.org/


Where is the Redactor files?
----------------------------

Unfortunately Redactor is not a Software Libre, so we could not pack
it into this application. You have to get it at
http://imperavi.com/redactor/download/ and copy the directory
containing the files ``redactor.min.js`` and ``redactor.css`` to some
directory specified at your ``STATICFILES_DIRS`` setting.


Using together ``django.contrib.admin``
---------------------------------------

Redator provides a CSS to improve the display of Redactor in your
*Django Admin*. Following is a example of how you can use it::

  from redator.widgets import RedactorEditorAdmin

  class MyModelAdmin(admin.ModelAdmin):
      formfield_overrides = {
          TextField: {'widget': RedactorEditorAdmin},
      }

Or you can simply inherit from ``redator.admin.RedactorAdmin`` as follow::

  from redator.admin import RedactorAdmin

  class MyModelAdmin(RedactorAdmin):
      ...
