#!/usr/bin/env python
# coding=utf-8

# beets-rgain – A replay gain plugin for Beets
#
# Copyright © 2013 Johan Kiviniemi <devel@johan.kiviniemi.name>
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

from setuptools import setup

setup(
    name='beets-rgain',
    version='0.1',
    description='rgain plugin for beets',
    author='Johan Kiviniemi',
    author_email='devel@johan.kiviniemi.name',
    url='http://github.com/ion1/beets-rgain',
    license='ISC',
    platforms='ALL',
    include_package_data=True,

    packages=['beetsplug', 'beetsscript'],
    namespace_packages=['beetsplug', 'beetsscript'],
    entry_points={
        'console_scripts': [
            'beets_rgain_helper = beetsscript.beets_rgain_helper:main',
        ],
    },

    install_requires=['pyyaml', 'rgain'],
)
