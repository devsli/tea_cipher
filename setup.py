#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from tea import __version__


with open('README.rst', 'rt') as doc:
    long_description = doc.read()

setup(
    name='tea',
    version=__version__,
    author='Amezoure',
    author_email='amezoure@gmail.com',
    description='Simple and fast symmetric-key algorithm cipher',
    long_description=long_description,
    license='MIT',
    url='https://github.com/amezoure/tea_cipher',
    packages=['tea'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Security :: Cryptography'
    ]
)
