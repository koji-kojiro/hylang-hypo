#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from hyapp import __version__

config = {
    'name': 'hypo',
    'author': 'koji-kojiro',
    'author_email': 'kojiro0531@gmail.com',
    'url': '',
    'description': '',
    'long_description': open('README.rst', 'r').read(),
    'license': 'MIT',
    'version': __version__,
    'install_requires': [],
    'classifiers': [
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 1 - Planning",
    ],
    'entry_points': "[console_scripts]\nhypo=hypo:main",
    'py_modules': ['hypo'],
}

if __name__ == '__main__':
    setup(**config)
