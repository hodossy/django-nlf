#!/usr/bin/env python

from setuptools import setup

from django_nlf import __version__ as dnlf_version


with open('README.md') as desc:
    LONG_DESCRIPTION = desc.read()

with open('requirements.txt') as reqs:
    REQUIREMENTS = reqs.readlines()

setup(
    name='django-nlf',
    version=dnlf_version,
    description='Django Natural Language Filter package',
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    maintainer='Hodossy, Szabolcs',
    maintainer_email='hodossy.szabolcs@gmail.com',
    url='https://github.com/hodossy/django-nlf',
    license='MIT',
    platforms='any',
    packages=['django_nlf'],
    keywords=['django', 'natural-Language', 'filtering'],
    install_requires=REQUIREMENTS,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Typing :: Typed',
    ],
    python_requires='>=3.6',
)
