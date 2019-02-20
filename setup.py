# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4
# BaruwaAPI Python bindings for Baruwa REST API
# Copyright (C) 2015-2019 Andrew Colin Kissa <andrew@topdog.za.net>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
"""
BaruwaAPI: Python bindings for Baruwa REST API

Copyright 2015-2019, Andrew Colin Kissa
Licensed under MPL 2.0.
"""
import os
import sys

try:
    import multiprocessing
    # Workaround for multiprocessing atexit exception bug
    assert multiprocessing
except ImportError:
    pass

from imp import load_source
from setuptools import setup, find_packages


TEST_REQUIRES = ['nose', 'coverage', 'mock']

if sys.version_info < (2, 7):
    TEST_REQUIRES.append('unittest2')


def get_readme():
    """Generate long description"""
    pandoc = None
    for path in os.environ["PATH"].split(os.pathsep):
        path = path.strip('"')
        pandoc = os.path.join(path, 'pandoc')
        if os.path.isfile(pandoc) and os.access(pandoc, os.X_OK):
            break
    try:
        if pandoc:
            cmd = [pandoc, '-t', 'rst', 'README.md']
            long_description = os.popen(' '.join(cmd)).read()
        else:
            raise ValueError
    except BaseException:
        long_description = open("README.md").read()
    return long_description


def main():
    """Main"""
    version = load_source("version", os.path.join("BaruwaAPI", "__init__.py"))

    opts = dict(
        name="BaruwaAPI",
        version=version.__version__,
        description="Python bindings for Baruwa REST API",
        long_description=get_readme(),
        keywords="baruwa api rest",
        author=version.__author__,
        author_email=version.__email__,
        url="https://github.com/baruwa-enterprise/BaruwaAPI",
        license="MPL 2.0",
        packages=find_packages(exclude=['tests']),
        include_package_data=True,
        zip_safe=False,
        tests_require=TEST_REQUIRES,
        test_suite='nose.collector',
        install_requires=['restkit'],
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
            'Natural Language :: English',
            'Operating System :: OS Independent'],
    )
    setup(**opts)


if __name__ == "__main__":
    main()
