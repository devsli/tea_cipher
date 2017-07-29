#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from tea_cipher import __version__


def InstallTeaCipher():
    setup(
        name='tea_cipher',
        version=__version__,
        description='Simple and fast symmetric-key algorithm cipher',
        long_description=open('README.rst', 'rt').read(),
        url='https://github.com/amezoure/tea_cipher',
        author='Amezoure',
        author_email='amezoure@gmail.com',
        license='MIT',
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Information Technology',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: Implementation :: CPython',
            'Topic :: Security :: Cryptography'
        ],
        keywords='cryptography encryption algorithms',
        packages=find_packages(),
        python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*')


if __name__ == '__main__':
    InstallTeaCipher()
