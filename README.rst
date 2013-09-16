==============
Django Redator
==============

**Django Redator** (sic) is a application for the `Django Web
Framework`_ to help you integrate `Redactor`_, a beautiful and
easy-to-use WYSIWYG HTML editor, into your projects.

*Tested on Redactor 9.1.4*

.. _`Django Web Framework`: http://www.djangoproject.com
.. _`Redactor`: http://imperavi.com/redactor/


Installing & Setup
==================

Redator is available on `Python Package Index (PyPI)`_ so you can
easily install the latest stable version of it using *pip*::

  pip instal django-redator

On your Django project you must add ``redator`` to your
``INSTALLED_APPS`` and configure your ``urls.py``::

  url(r'^_redator/', include('redator.urls', namespace='redactor', app_name='redator')),

You also have to create the database tables::

  python manage.py syncdb --migrate


Forms
-----

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

.. _`Python Package Index (PyPI)`: http://pypi.python.org/


Admin
-----

Django Redator also provides a widget to you use on ``ModelAdmin``. It
just add some CSS rules to display it better on Admin::

  from redator.widgets import RedactorEditorAdmin

  class MyModelAdmin(admin.ModelAdmin):
      formfield_overrides = {
          TextField: {'widget': RedactorEditorAdmin(
              attrs={'rows': 40}
          )},
      }

      class Media:
          js = ('//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js',)


Settings
--------

You might want to change the settings of app and Redactor editor and
there is two ways to do that.

Changing the defaults, globally, on your ``settings.py``::

  REDATOR_UPLOAD_TO = 'redator/%Y-%m/'
  REDATOR_REDACTOR_OPTIONS = {
    'wym': True,
    'autoresize': False
  }

Or changing per widget, that will override the global settings::

  class PostForm(forms.Form)
        body = forms.CharField(widget=RedactorEditor(
            upload_to='post/%Y-%m/',
            redactor_options={
                'wym': False,
            }
        ))
        ...
  

Where is the Redactor files?
----------------------------

Unfortunately Redactor is not a Software Libre, so we could not pack
it into this application. You have to get it at
http://imperavi.com/redactor/download/ and copy the directory
containing the files ``redactor.min.js`` and ``redactor.css`` to some
directory specified at your ``STATICFILES_DIRS`` setting.


License
=======

Django Redator
--------------

| Copyright (c) 2012-, Guilherme Gondim
| Copyright (c) 2010-2012 Vladimir Sidorenko

Django Redator is Software Libre; you can redistribute it and/or modify
it under the terms of the BSD (3-clause) License.

You should have received a copy of the BSD License along with this
program; see the file LICENSE.


Redactor
--------

Redactor itself is created by `Imperavi`_.
You can read about it's licensing at http://imperavi.com/redactor/

.. _`Imperavi`: hhttp://imperavi.com/
