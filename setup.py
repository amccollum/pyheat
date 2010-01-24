#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Python OpenGL Heatmap Library"""


try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages


classifiers = """\
Development Status :: 3 - Alpha
Environment :: Console
Environment :: Web Environment
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Programming Language :: Python
Topic :: Software Development :: Libraries :: Python Modules
"""

doc_lines = __doc__.split('\n')


setup(
    name='PyHeat',
    version='0.1',
    description='OpenGL Heatmap Library',
    author='Andrew McCollum',
    author_email='amccollum@gmail.com',
    license='MIT',
    url='http://github.com/amccollum/pyheat',
    packages=find_packages(exclude=['ez_setup']),
    zip_safe=False,
    install_requires=[
        'PyOpenGL',
        'PIL',
        ],
    )
