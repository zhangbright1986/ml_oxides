#!/usr/bin/env python
from distutils.core import setup
import os

def readme():
    with open('README.rst') as f:
        return f.read()

packages = []
for dirname, dirnames, filenames in os.walk('mlox'):
    if '__init__.py' in filenames:
        packages.append(dirname.replace('/', '.'))

setup(name='mlox',
      version='1.0',
      description='Package for ML of Oxides',
      long_description=readme(),
      author='Liang Zhang',
      author_email='zhangbright1986@gmail.com',
      packages=packages,
      )
