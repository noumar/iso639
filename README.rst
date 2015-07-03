ISO639
======

ISO 639 library for Python.

Status
------

|master_status| |dev_status| |pypi_month| |pypi_version| |gh_forks| |gh_stars|

License
-------

GNU Affero General Public License version 3 (AGPLv3)

Supports
--------

-  ISO 639-1
-  ISO 639-2
-  ISO 639-3
-  ISO 639-5

Breaking changes
----------------

-  0.4.1: ISO 639-3 files updated
-  0.4.0: ``alpha3`` has been renamed to ``part3``. ``languages.alpha3`` might be used as an aggregation of all ‘three letter codes’ in the future.

Compatibility
-------------

This library is aimed to be fully compatible with ``pycountry.languages`` v1.11 and before. v1.12 broke their own API and this library will **not** support the new API.

It provides the following attribute abstractions:

-  ``terminology`` -> ``part2t``
-  ``bibliographic`` -> ``part2b``
-  ``alpha2`` -> ``part1``

If you have no intentions on using ``pycountry.languages`` or want/need to keep compatibility then please use the ``partX`` attributes for brevity and clarity.

Contains external data
----------------------

-  `ISO 639-1`_, on 2014-11-28
-  `ISO 639-2`_, on 2014-11-28
-  `ISO 639-3 Code Set`_, dated 2015-01-12
-  `ISO 639-3 Language Names Index`_, dated 2015-01-12
-  `ISO 639-3 Macrolanguage Mappings`_, dated 2015-01-12
-  `ISO 639-3 Retired Code Element Mappings`_, dated 2015-01-12
-  `ISO 639-5`_, dated 2011-05-12

.. _ISO 639-1: http://id.loc.gov/vocabulary/iso639-1.tsv
.. _ISO 639-2: http://id.loc.gov/vocabulary/iso639-2.tsv
.. _ISO 639-3 Code Set: http://www-01.sil.org/iso639-3/iso-639-3.tab
.. _ISO 639-3 Language Names Index: http://www-01.sil.org/iso639-3/iso-639-3_Name_Index.tab
.. _ISO 639-3 Macrolanguage Mappings: http://www-01.sil.org/iso639-3/iso-639-3-macrolanguages.tab
.. _ISO 639-3 Retired Code Element Mappings: http://www-01.sil.org/iso639-3/iso-639-3_Retirements.tab
.. _ISO 639-5: http://id.loc.gov/vocabulary/iso639-5.tsv

.. |master_status| image:: https://travis-ci.org/noumar/iso639.svg?branch=master
    :target: https://travis-ci.org/noumar/iso639
    :alt: master
.. |dev_status| image:: https://travis-ci.org/noumar/iso639.svg?branch=development
    :target: https://travis-ci.org/noumar/iso639
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
