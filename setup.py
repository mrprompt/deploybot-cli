#!/usr/bin/env python
# -*- coding: utf-8 -*-
from codecs import open as codecs_open
from setuptools import setup


# Get the long description from the relevant file
with codecs_open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="deploybot-cli",
    packages=['deploybot', 'test'],
    test_suite='test',
    version='0.0.2',
    description=u"Deploybot API Client",
    long_description=long_description,
    classifiers=[],
    keywords='deploy,service,api,client,cli,deploybot,continuous,delivery,cd',
    author=u"Thiago Paes",
    author_email='mrprompt@gmail.com',
    url='https://github.com/mrprompt/deploybot-cli',
    license='GPL',
    include_package_data=True,
    zip_safe=False,
    install_requires=[
      'click', 'python-http-client'
    ],
    entry_points="""
    [console_scripts]
    deploybot-cli=cli.py
    """
)
