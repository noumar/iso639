"""
Python library for ISO 639-3 standard

Copyright (c) 2014 Mikael Karlsson (CSC - IT Center for Science Ltd.).
Licensed under AGPLv3.
"""

from setuptools import setup, find_packages

setup(
    name='iso_639_3',
    version='0.1',
    description="Python library for ISO 639-3 standard",
    long_description=
    """
    """,
    classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='pycountry language iso-639-3 iso 639 639-3',
    author='Mikael Karlsson',
    author_email='i8myshoes@gmail.com',
    url='https://github.com/noumar/iso_639_3/',
    license='AGPLv3',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    package_data={'': ['*.tab']},
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    entry_points=
    """
    """,
)
