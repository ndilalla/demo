import os

PACKAGE_NAME = 'demo'

DEMO_ROOT = os.path.abspath(os.path.dirname(__file__))

DEMO_DATA = os.path.join(DEMO_ROOT, 'data')
from . import _version
__version__ = _version.get_versions()['version']
