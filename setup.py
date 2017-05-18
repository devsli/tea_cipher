#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from tea import __version__


setup(
    name='tea',
    version=__version__,
    author='Amezoure',
    author_email='amezoure@gmail.com',
    license='MIT',
    url='https://github.com/amezoure/tea',
    packages=find_packages(),
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Security :: Cryptography'
    )
)
