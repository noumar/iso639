"""
Python library for ISO 639 standard

Copyright (c) 2014 Mikael Karlsson (CSC - IT Center for Science Ltd.).
Licensed under AGPLv3.
"""


def _fabtabular():
    """
    This function retrieves the ISO 639 and inverted names datasets as tsv files and returns them as two lists.
    """
    import csv
    import sys
    from pkg_resources import resource_filename

    data = resource_filename(__package__, 'iso-639-3.tab')
    inverted = resource_filename(__package__, 'iso-639-3_Name_Index.tab')

    if sys.version_info[0] == 2:
        # from urllib2 import urlopen
        # u = urlopen('http://www-01.sil.org/iso639%2D3/iso-639-3.tab')
        u = open(data)
        # i = urlopen('http://www-01.sil.org/iso639-3/iso-639-3_Name_Index.tab')
        i = open(inverted)
        return list(csv.reader(u, delimiter='\t'))[1:], list(csv.reader(i, delimiter='\t'))[1:]
    else:
        # from urllib.request import urlopen
        # import io
        # with io.StringIO(urlopen('http://www-01.sil.org/iso639%2D3/iso-639-3.tab').read().decode()) as u, \
        #         io.StringIO(urlopen('http://www-01.sil.org/iso639-3/iso-639-3_Name_Index.tab').read().decode()) as i:
        with open(data) as u, \
                open(inverted) as i:
            return list(csv.reader(u, delimiter='\t'))[1:], list(csv.reader(i, delimiter='\t'))[1:]


class _Language(object):
    """
    This class represents a language. It imitates pycountry's language class structure.
    """
    def __init__(self, dash3, dash2b, dash2t, dash1, name, inverted):
        self.alpha3 = dash3
        self.bibliographic = dash2b
        self.terminology = dash2t
        self.alpha2 = dash1
        self.name = name
        self.inverted = inverted


class Iso639(object):
    """
    This class is a close to drop-in replacement for pycountry.languages.
    But unlike pycountry.languages it also supports ISO 639-3.
    It implements the Singleton design pattern for performance reasons.
    """
    __instance = None
    _languages = None
    _alpha3 = None
    _bibliographic = None
    _terminology = None
    _alpha2 = None
    _name = None
    _inverted = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(cls, cls).__new__(cls)
        return cls.__instance

    @property
    def languages(self):
        if self._languages is None:
            l, i = _fabtabular()
            self._languages = [_Language(a, b, c, d, e, [x[2] for x in i if x[0] == a][0])
                               for a, b, c, d, _, _, e, _ in l]
        return self._languages

    @property
    def alpha3(self):
        if self._alpha3 is None:
            self._alpha3 = {x.alpha3: x for x in self.languages if x.alpha3}
        return self._alpha3

    @property
    def bibliographic(self):
        if self._bibliographic is None:
            self._bibliographic = {x.bibliographic: x for x in self.languages if x.bibliographic}
        return self._bibliographic

    @property
    def terminology(self):
        if self._terminology is None:
            self._terminology = {x.terminology: x for x in self.languages if x.terminology}
        return self._terminology

    @property
    def alpha2(self):
        if self._alpha2 is None:
            self._alpha2 = {x.alpha2: x for x in self.languages if x.alpha2}
        return self._alpha2

    @property
    def name(self):
        if self._name is None:
            self._name = {x.name: x for x in self.languages if x.name}
        return self._name

    @property
    def inverted(self):
        if self._inverted is None:
            self._inverted = {x.inverted: x for x in self.languages if x.inverted}
        return self._inverted

    def get(self, **kwargs):
        """
        A simple getter function for languages. Takes 1 keyword/value and returns 1 language object.
        """
        if not len(kwargs) == 1:
            raise AttributeError('Only one keyword expected')
        key, value = kwargs.popitem()
        return getattr(self, key)[value]
