"""
Convert languages and language codes into ISO names

Copyright (C) 2014 Mikael Karlsson.
Licensed under AGPLv3.
"""

import re


def map_language(language):
    if '_' in language:
        language = language.split('_')[0]
    if len(language) == 2:
        try: return languages.get(alpha2=language.lower())
        except KeyError: pass
    elif len(language) == 3:
        if dash3:
            try: return languages.get(alpha3=language.lower())
            except KeyError: pass
        try: return languages.get(terminology=language.lower())
        except KeyError: pass
        try: return languages.get(bibliographic=language.lower())
        except KeyError: pass
    else:
        try: return languages.get(name=language.title())
        except KeyError: pass
        for l in re.split('[,.;: ]+', language):
            try: return languages.get(name=l.title())
            except KeyError: pass


class iso_639_3(object):
    """
    This class is a close to drop-in replacement for pycountry.languages.
    But unlike pycountry.languages it also supports ISO 639-3.
    """
    def __init__(self):
        l, i = self._fabtabular()
        self.languages = [self.language(a, b, c, d, e, [x[2] for x in i if x[0] == a][0])
                          for a, b, c, d, _, _, e, _ in l]
        self.alpha3 = {x.alpha3: x for x in self.languages if x.alpha3}
        self.bibliographic = {x.bibliographic: x for x in self.languages if x.bibliographic}
        self.terminology = {x.terminology: x for x in self.languages if x.terminology}
        self.alpha2 = {x.alpha2: x for x in self.languages if x.alpha2}
        self.name = {x.name: x for x in self.languages if x.name}
        self.inverted = {x.inverted: x for x in self.languages if x.inverted}

    class language(object):
        def __init__(self, dash3, dash2b, dash2t, dash1, name, inverted):
            self.alpha3 = dash3
            self.bibliographic = dash2b
            self.terminology = dash2t
            self.alpha2 = dash1
            self.name = name
            self.inverted = inverted

    def get(self, **kwargs):
        if not len(kwargs) == 1:
            raise AttributeError("Only one keyword expected")
        key, value = kwargs.popitem()
        return getattr(self, key)[value]

    @staticmethod
    def _fabtabular():
        import csv
        import sys

        if sys.version_info[0] == 2:
            # from urllib2 import urlopen
            # u = urlopen('http://www-01.sil.org/iso639%2D3/iso-639-3.tab')
            u = open('iso-639-3.tab')
            # i = urlopen('http://www-01.sil.org/iso639-3/iso-639-3_Name_Index.tab')
            i = open('http://www-01.sil.org/iso639-3/iso-639-3_Name_Index.tab')
            return list(csv.reader(u, delimiter='\t'))[1:], list(csv.reader(i, delimiter='\t'))[1:]
        else:
            # from urllib.request import urlopen
            # import io
            # with io.StringIO(urlopen('http://www-01.sil.org/iso639%2D3/iso-639-3.tab').read().decode()) as u, \
            #         io.StringIO(urlopen('http://www-01.sil.org/iso639-3/iso-639-3_Name_Index.tab').read().decode()) as i:
            with open('iso-639-3.tab') as u, \
                    open('iso-639-3_Name_Index.tab') as i:
                return list(csv.reader(u, delimiter='\t'))[1:], list(csv.reader(i, delimiter='\t'))[1:]


""" Use ISO 639-3 ?? """
dash3 = True

if dash3:
    languages = iso_639_3()
else:
    from pycountry import languages

english = languages.get(name='English')
chinese = languages.get(name='Chinese')
arabic = languages.get(name='Arabic')

assert(map_language('english') is english)
assert(map_language('English') is english)
assert(map_language('eNgLiSh') is english)
assert(map_language('Eng') is english)
assert(map_language('eNg') is english)
assert(map_language('enG') is english)
assert(map_language('ENG') is english)
assert(map_language('eng') is english)
assert(map_language('En') is english)
assert(map_language('EN') is english)
assert(map_language('eN') is english)
assert(map_language('en') is english)
assert(map_language('En_Us') is english)
assert(map_language('EN_US') is english)
assert(map_language('en_us') is english)

assert(map_language('zho') is chinese)
assert(map_language('chi') is chinese)

assert(map_language('ara') is arabic)
assert(map_language('Arabic, Moroccan Spoken') is arabic)

if dash3:
    moroccan = languages.get(name='Moroccan Arabic')
    tzeltal = languages.get(name='Tzeltal')
    assert(map_language('ary') is moroccan)
    assert(languages.alpha3['ary'] is moroccan)
    assert(languages.get(alpha3='ary') is moroccan)
    assert(map_language('Moroccan Arabic') is moroccan)
    assert(map_language('Tzeltal') is tzeltal)
    assert(map_language('tzh') is tzeltal)
else:
    assert(map_language('Moroccan Arabic') is arabic)