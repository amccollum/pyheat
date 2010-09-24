#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Python OpenGL Heatmap Library"""

from distutils.core import setup


classifiers = """\
Programming Language :: Python
License :: OSI Approved :: MIT License
Operating System :: OS Independent
Development Status :: 3 - Alpha
Environment :: Console :: Framebuffer
Environment :: Web Environment
Intended Audience :: Developers
Topic :: Software Development :: Libraries :: Python Modules
Topic :: Multimedia :: Graphics"""

setup(
    name='PyHeat',
    version='0.1',
    description='OpenGL Heatmap Library',
    classifiers=classifiers.split('\n'),
    author='Andrew McCollum',
    author_email='amccollum@gmail.com',
    license='MIT',
    url='http://github.com/amccollum/pyheat',
    packages=['pyheat'],
    requires=[
        'PyOpenGL',
        'PIL',
        ],
    )
