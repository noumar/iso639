"""
Python library for ISO 639 standard

Copyright (c) 2014 Mikael Karlsson (CSC - IT Center for Science Ltd.).
Licensed under AGPLv3.
"""

import collections
import csv
from pkg_resources import resource_filename

# Fix for Python 3.0 - 3.2
if not __package__:
    __package__ = __name__.split('.')[0]


def _fabtabular():
    """
    This function retrieves the ISO 639 and inverted names datasets as tsv files and returns them as two lists.
    """
    import sys

    data = resource_filename(__package__, 'iso-639-3.tab')
    inverted = resource_filename(__package__, 'iso-639-3_Name_Index.tab')
    macro = resource_filename(__package__, 'iso-639-3-macrolanguages.tab')

    # if sys.version_info[0] == 2:
    #     from urllib2 import urlopen
    #     from contextlib import closing
    #     data_fo = closing(urlopen('http://www-01.sil.org/iso639-3/iso-639-3.tab'))
    #     inverted_fo = closing(urlopen('http://www-01.sil.org/iso639-3/iso-639-3_Name_Index.tab'))
    # else:
    #     from urllib.request import urlopen
    #     import io
    #     data_fo = io.StringIO(urlopen('http://www-01.sil.org/iso639-3/iso-639-3.tab').read().decode())
    #     inverted_fo = io.StringIO(urlopen('http://www-01.sil.org/iso639-3/iso-639-3_Name_Index.tab').read().decode())
    data_fo = open(data)
    inverted_fo = open(inverted)
    macro_fo = open(macro)
    with data_fo as u:
        with inverted_fo as i:
            with macro_fo as m:
                return (list(csv.reader(u, delimiter='\t'))[1:],
                        list(csv.reader(i, delimiter='\t'))[1:],
                        list(csv.reader(m, delimiter='\t'))[1:])


class _Language(object):
    """
    This class represents a language. It imitates pycountry's language class structure.
    """
    def __init__(self, dash3, dash2b, dash2t, dash1, name, inverted, macro):
        self.alpha3 = dash3
        self.bibliographic = dash2b
        self.terminology = dash2t
        self.alpha2 = dash1
        self.name = name
        self.inverted = inverted
        self.macro = macro


class lazy_property(object):
    """
    Implements a lazy property decorator, that overwrites itself/property with value
    """
    def __init__(self, f):
        self.f = f
        self.name = f.__name__

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        val = self.f(instance)
        setattr(instance, self.name, val)
        return val


class Iso639(object):
    """
    This class is a close to drop-in replacement for pycountry.languages.
    But unlike pycountry.languages it also supports ISO 639-3.

    It implements the Singleton design pattern for performance reasons.
    Is uses lazy properties for faster import time.
    """

    def __new__(cls):
        if not hasattr(cls, '__instance'):
            setattr(cls, '__instance', super(cls, cls).__new__(cls))
        return getattr(cls, '__instance')

    def __len__(self):
        return len(self.languages)

    def __iter__(self):
        return iter(self.languages)

    @lazy_property
    def languages(self):
        l, i, m = _fabtabular()
        i = dict((x[0], x) for x in i)
        m = dict((x[1], x) for x in m)
        return [_Language(a, b, c, d, e,
                          i.get(a, ['', '', ''])[2],
                          m.get(a, [''])[0])
                for a, b, c, d, _, _, e, _ in l]

    @lazy_property
    def alpha3(self):
        return dict((x.alpha3, x) for x in self.languages if x.alpha3)

    @lazy_property
    def bibliographic(self):
        return dict((x.bibliographic, x) for x in self.languages if x.bibliographic)

    @lazy_property
    def terminology(self):
        return dict((x.terminology, x) for x in self.languages if x.terminology)

    @lazy_property
    def alpha2(self):
        return dict((x.alpha2, x) for x in self.languages if x.alpha2)

    @lazy_property
    def name(self):
        return dict((x.name, x) for x in self.languages if x.name)

    @lazy_property
    def inverted(self):
        return dict((x.inverted, x) for x in self.languages if x.inverted)

    @lazy_property
    def macro(self):
        m = collections.defaultdict(list)
        for x in self.languages:
            if x.macro:
                m[x.macro].append(x)
        return dict(m)

    @lazy_property
    def retired(self):
        def gen():
            with open(resource_filename(__package__, 'iso-639-3_Retirements.tab')) as rf:
                rtd = list(csv.reader(rf, delimiter='\t'))[1:]
                rc = [r[0] for r in rtd]
                for i, _, _, m, s, _ in rtd:
                    if m and m not in rc:
                        yield i, self.get(alpha3=m)
                    else:
                        yield i, s

        return dict(gen())

    def get(self, **kwargs):
        """
        A simple getter function for languages. Takes 1 keyword/value and returns 1 language object.
        """
        if not len(kwargs) == 1:
            raise AttributeError('Only one keyword expected')
        key, value = kwargs.popitem()
        return getattr(self, key)[value]
