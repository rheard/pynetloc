__author__ = ()
__version__ = "0.0.1"

from setuptools import setup


setup(name='pynetloc',
      version=__version__,
      description="A light Pythonic wrapper around .NET's GeoLocation libraries.",
      url='TBD',
      packages=['netloc'],
      install_requires=['expanded-pythonnet'])
