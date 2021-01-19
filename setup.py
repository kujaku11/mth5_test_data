#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

setup_requirements = [
    "pytest-runner",
]

test_requirements = [
    "pytest>=3",
]

setup(
    author="Jared Peacock",
    author_email="jpeacock@usgs.gov",
    python_requires=">=3.5",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Test data for MTH5",
    license="MIT license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="mth5_test_data",
    name="mth5_test_data",
    setup_requires=setup_requirements,
    url="https://github.com/kujaku11/mth5_test_data",
    version="0.1.0",
    zip_safe=False,
)
