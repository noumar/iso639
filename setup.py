"""
Python library for ISO 639 standard

Copyright (c) 2014-2016 Mikael Karlsson (CSC - IT Center for Science Ltd.).
Licensed under AGPLv3.
"""

import sys
from setuptools import setup, find_packages
from iso639 import __version__

if sys.version_info[0] == 3:
    from functools import partial

    global open
    open = partial(open, encoding='utf-8')

with open('README.rst') as f:
    for _ in range(5):
        f.readline()
    long_description = f.read()

setup(
    name='iso-639',
    version=__version__,
    description="Python library for ISO 639 standard",
    long_description=long_description,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Text Processing :: Linguistic',
    ],
    keywords='pycountry languages iso-639 iso 639 639-1 639-2 639-3 639-5',
    author='Mikael Karlsson',
    author_email='i8myshoes@gmail.com',
    url='https://github.com/noumar/iso639',
    license='AGPL-3.0',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    package_data={'': ['*.tab', '*.tsv']},
    zip_safe=False,
    install_requires=[],
    entry_points=
    """
    """,
)
