#!/usr/bin/env python
"""
A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleprojecta

#import pathlib
#here = pathlib.Path(__file__).parent.resolve()
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

setup(
    author="MTH5 Team",
    author_email="jpeacock@usgs.gov",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    name='mth5_test_data',
    version='0.0.1', 
    description='A place to keep data samples used in testing mth5 to avoid bloat during development',
    url='https://github.com/kujaku11/mth5_test_data',
    keywords='mth5, data, examples',
    packages=find_packages(include=['mth5_test_data', 'mth5_test_data.*']),  # Required
) 

