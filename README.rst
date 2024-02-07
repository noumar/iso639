ISO639
======

ISO 639 library for Python.

Status
------

|master_status| |dev_status| |pypi_month| |pypi_version| |gh_forks| |gh_stars|

License
-------

GNU Affero General Public License version 3.0 only (AGPL-3.0-only)

Supports
--------

- ISO 639-1
- ISO 639-2
- ISO 639-3
- ISO 639-5

Breaking changes
----------------

- 0.4.4: ``retired`` has been changed to { 'code': (``datetime``, [``_Language``, ...], 'description') }.
- 0.4.0: ``alpha3`` has been renamed to ``part3``. ``languages.alpha3`` might be used as an aggregation of all 'three letter codes' in the future.

Compatibility
-------------

This library is aimed to be **fully compatible** with ``pycountry.languages`` v1.11 and before. In v1.12 they broke their own API and this library will **not support** the new API.

It provides the following attribute abstractions:

- ``terminology`` -> ``part2t``
- ``bibliographic`` -> ``part2b``
- ``alpha2`` -> ``part1``

If you have no intentions on using ``pycountry.languages`` or want/need to keep compatibility then please use the ``partX`` attributes for brevity and clarity.

Usage
-----

As taken from ``pycountry.languages`` v1.11 documentation, with modifications and further additions.

.. code-block:: python

    >>> from iso639 import languages
    >>> from pprint import pprint

    >>> len(languages)
    7981

    >>> type(list(languages)[0])
    <class 'iso639.iso639._Language'>

    # Compatibility
    >>> aragonese = languages.get(alpha2='an')
    >>> aragonese.alpha2
    'an'
    >>> aragonese.bibliographic
    'arg'
    >>> aragonese.terminology
    'arg'
    >>> aragonese.name
    'Aragonese'

    >>> bengali = languages.get(alpha2='bn')
    >>> bengali.name
    'Bengali'

    # We *do not* deviate from the standard
    >>> try:
    ...     bengali.common_name
    ... except AttributeError as e:
    ...     print(e)
    '_Language' object has no attribute 'common_name'

    # New API
    >>> aragonese = languages.get(part1='an')
    >>> aragonese.part1
    'an'
    >>> aragonese.part2b
    'arg'
    >>> aragonese.part2t
    'arg'
    >>> aragonese.part3
    'arg'
    >>> aragonese.name
    'Aragonese'
    >>> aragonese.inverted
    'Aragonese'
    >>> pprint(vars(aragonese))
    {'inverted': 'Aragonese',
     'macro': '',
     'name': 'Aragonese',
     'names': [],
     'part1': 'an',
     'part2b': 'arg',
     'part2t': 'arg',
     'part3': 'arg',
     'part5': ''}
     >>> pprint(vars(languages.get(name="French")))
     {'inverted': 'French',
      'macro': '',
      'name': 'French',
      'names': [],
      'part1': 'fr',
      'part2b': 'fre',
      'part2t': 'fra',
      'part3': 'fra',
      'part5': ''}
     >>> sanapana = languages.get(retired='sap')
     >>> [type(elem).__name__ for elem in sanapana]
     ['datetime', 'list', 'str']
     >>> [lang.part3 for lang in sanapana[1]]
     ['spn', 'aqt']

Contains external data
----------------------

- `ISO 639-1`_, on 2014-11-28
- `ISO 639-2`_, on 2014-11-28
- `ISO 639-3 Code Set`_, dated 2015-05-05
- `ISO 639-3 Language Names Index`_, dated 2015-05-05
- `ISO 639-3 Macrolanguage Mappings`_, dated 2015-05-05
- `ISO 639-3 Retired Code Element Mappings`_, dated 2015-05-05
- `ISO 639-5`_, dated 2011-05-12

.. _ISO 639-1: http://id.loc.gov/vocabulary/iso639-1.tsv
.. _ISO 639-2: http://id.loc.gov/vocabulary/iso639-2.tsv
.. _ISO 639-3 Code Set: http://www-01.sil.org/iso639-3/iso-639-3.tab
.. _ISO 639-3 Language Names Index: http://www-01.sil.org/iso639-3/iso-639-3_Name_Index.tab
.. _ISO 639-3 Macrolanguage Mappings: http://www-01.sil.org/iso639-3/iso-639-3-macrolanguages.tab
.. _ISO 639-3 Retired Code Element Mappings: http://www-01.sil.org/iso639-3/iso-639-3_Retirements.tab
.. _ISO 639-5: http://id.loc.gov/vocabulary/iso639-5.tsv

.. |master_status| image:: https://travis-ci.org/noumar/iso639.svg?branch=master
    :target: https://travis-ci.org/noumar/iso639/branches
    :alt: master
.. |dev_status| image:: https://travis-ci.org/noumar/iso639.svg?branch=development
    :target: https://travis-ci.org/noumar/iso639/branches
    :alt: development
.. |pypi_month| image:: https://img.shields.io/pypi/dm/iso-639.svg
    :target: https://pypi.python.org/pypi/iso-639
    :alt: downloads/month
.. |pypi_version| image:: https://img.shields.io/pypi/v/iso-639.svg
    :target: https://pypi.python.org/pypi/iso-639
    :alt: latest version
.. |gh_forks| image:: https://img.shields.io/github/forks/noumar/iso639.svg
    :target: https://github.com/noumar/iso639/network
    :alt: gh forks
.. |gh_stars| image:: https://img.shields.io/github/stars/noumar/iso639.svg
    :target: https://github.com/noumar/iso639/stargazers
    :alt: gh stars
