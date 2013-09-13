#/usr/bin/env python

import codecs
import os
import sys

from setuptools import setup, find_packages


if 'publish' in sys.argv:
    os.system('python setup.py sdist upload')
    sys.exit()

read = lambda filepath: codecs.open(filepath, 'r', 'utf-8').read()


# Dynamically calculate the version based on redator.VERSION.
version = __import__('redator').get_version()

setup(
    name='django-redator',
    version=version,
    description=(
        'Django Redator (sic) helps you integrate Redactor '
        '<http://imperavi.com/redactor/> to your Django forms. Redactor '
        'is a beautiful and easy-to-use WYSIWYG HTML editor.'
    ),
    long_description=read(os.path.join(os.path.dirname(__file__), 'README.rst')),
    keywords = 'django app wysiwyg editor redactor',
    author='Vladimir Sidorenko, Guilherme Gondim',
    author_email='semente+django-redator@taurinus.org',
    maintainer='Guilherme Gondim',
    maintainer_email='semente+django-redator@taurinus.org',
    license='BSD License',
    url='https://bitbucket.org/semente/django-redator/',
    download_url='https://bitbucket.org/semente/django-redator/downloads/',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    #install_requires=[],
)
