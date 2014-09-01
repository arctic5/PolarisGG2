from distutils.core import setup
import py2exe, sys, os
import glob
sys.argv.append('py2exe')

setup(
    options = {'py2exe': {'bundle_files': 1, 'compressed': True}},
    console = [{'script': "server.py"}],
    zipfile = None,
    data_files=[('.', glob.glob('*.dll'))],
)