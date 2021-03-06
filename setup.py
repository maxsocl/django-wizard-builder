#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from wizard_builder import __version__ as version

from setuptools import setup, find_packages

if sys.argv[-1] == 'publish':
    try:
        import wheel
        print("Wheel version: ", wheel.__version__)
    except ImportError:
        print('Wheel library missing. Please run "pip install wheel"')
        sys.exit()
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()

if sys.argv[-1] == 'tag':
    print("Tagging the version on github:")
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='django-wizard-builder',
    version=version,
    description='Create multi-page wizard with branching logic from the Django admin, no code required.',
    long_description=readme + '\n\n' + history,
    author='Sexual Health Innovations',
    author_email='tech@sexualhealthinnovations.org',
    url='https://github.com/SexualHealthInnovations/django-wizard-builder',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'django-formtools>=2.0',
        'django-model-utils>=3.0',
    ],
    license="BSD",
    zip_safe=False,
    keywords='django-wizard-builder',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
