import os
import sys
import platform

from setuptools import setup


version = '0.0.0'

with open('README.rst') as f:
    readme = f.read()

setup(
    name='pyq',
    version=version,
    author='Zhao Jiarong',
    author_email='kawing.chiu.sysu@gmail.com',
    url='',
    description="",
    long_description=readme,
    license='GNU Affero GPL v3.0',
    packages=['pyq'],
    install_requires=[],
    classifiers=[],
)
