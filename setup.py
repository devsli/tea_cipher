#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from tea_cipher import __version__


setup(
    name='tea_cipher',
    version=__version__,
    url='https://github.com/amezoure/tea_cipher',
    author='Amezoure',
    author_email='amezoure@gmail.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Security :: Cryptography'
    ],
    license='MIT',
    description='Simple and fast symmetric-key algorithm cipher',
    long_description=open('README.rst', 'rt').read(),
    keywords='cryptography encryption algorithms',
    platforms=['any'],
    zip_safe=False,
    packages=['tea_cipher'],
)
