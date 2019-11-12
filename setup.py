# -*- coding: utf-8 -*-
import setuptools


setuptools.setup(
    name='find_old_pages_in_dokuwiki',
    version='2019.1',
    license='Apache Software License 2.0',
    long_description=open('README.md').read(),
    packages=setuptools.find_packages(),
    zip_safe = False,
    install_requires=[
    ],

    include_package_data=True,

    entry_points={
        'console_scripts': [
            'find_old_pages_in_dokuwiki=find_old_pages_in_dokuwiki:main',
        ],
    }
)
