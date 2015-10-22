#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('requirements.txt') as req_file:
    requirements = req_file.read().split('\n')

with open('requirements-dev.txt') as req_file:
    requirements_dev = req_file.read().split('\n')

with open('VERSION') as fp:
    version = fp.read().strip()

setup(
    name='{{cookiecutter.package_name}}',
    version=version,
    description="{{cookiecutter.project_short_description}}",
    long_description=readme,
    author="{{cookiecutter.author}}",
    author_email='{{cookiecutter.author_email}}',
    url='{{cookiecutter.project_url}}',
    packages=[
        '{{cookiecutter.package_name}}',
    ],
    package_dir={'{{cookiecutter.package_name}}':
                 '{{cookiecutter.package_name}}'},
    include_package_data=True,
    install_requires=requirements,
    license="{{cookiecutter.license}}",
    zip_safe=False,
    keywords='{{cookiecutter.package_name}}',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
    ]
)
