from setuptools import setup
import os
import sys

#_here = os.path.abspath(os.path.dirname(__file__))


#if sys.version_info[0] < 3:
#    with open(os.path.join(_here, 'README.rst')) as f:
#        long_description = f.read()
#else:
#    with open(os.path.join(_here, 'README.rst'), encoding='utf-8') as f:
#        long_description = f.read()
#
#version = {}
#with open(os.path.join(_here, 'theOravle', 'version.py')) as f:
#    exec(f.read(), version)

setup(
    name='theOravle',
    version='0.0.1',
    description='Show how to structure a Python project.',
    long_description=readme,
    author='Thomas Maltesen',
    author_email='mcl868@alumni.ku.dk',
    url='https://github.com/mcl68/theOravle',
    license='GNU-3.0',
    packages=['theOravle'],
#   no dependencies in this example
   install_requires=['random','time' ],
#   no scripts in this example
#   scripts=['bin/a-script'],
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6'],
    )
