"""
Python library for ISO 639 standard

Copyright (c) 2014-2015 Mikael Karlsson (CSC - IT Center for Science Ltd.).
Licensed under AGPLv3.
"""

from setuptools import setup, find_packages

setup(
    name='iso639',
    version='0.4.1',
    description="Python library for ISO 639 standard",
    long_description=open('README.rst').read(),
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
    keywords='pycountry language iso-639 iso 639 639-1 639-2 639-3 639-5',
    author='Mikael Karlsson',
    author_email='i8myshoes@gmail.com',
    url='https://github.com/noumar/iso639',
    license='AGPLv3',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    package_data={'': ['*.tab', '*.tsv']},
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    entry_points=
    """
    """,
)
