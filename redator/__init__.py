VERSION = (0, 1)


def get_version():
    """Returns the version as a human-format string.
    """
    return '.'.join([str(i) for i in VERSION])


__license__ = 'BSD License'
__url__ = 'https://bitbucket.org/semente/django-redator'
__version__ = get_version()
