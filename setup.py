#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name="deploybot-cli",
    packages=['deploybot', 'test'],
    test_suite='test',
    version='0.2.5',
    description=u"Deploybot API Client",
    long_description=u"Deploybot terminal tool",
    classifiers=[],
    keywords='deploy,service,api,client,cli,deploybot,continuous,delivery,cd',
    author=u"Thiago Paes",
    author_email='mrprompt@gmail.com',
    url='https://github.com/mrprompt/deploybot-cli',
    license='GPL',
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'python_http_client', 'tableprint', 'click'
    ],
    extras_require={
        'test': ['pytest', 'pytest-cov', 'mock'],
    },
    entry_points={
        'console_scripts': [
            'deploybot-cli=deploybot.scripts.cli:main'
        ]
    }
)
