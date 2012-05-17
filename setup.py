#/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name="django-redactor",
    version="0.4",
    description="Django application for http://imperavi.ru/redactor/",
    author="Vladimir Sidorenko",
    author_email="yoyavova@gmail.com",
    license='BSD License',
    packages=find_packages(),
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
)
