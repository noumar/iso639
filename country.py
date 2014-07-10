"""
Convert languages and language codes into ISO names

Copyright (C) 2014 Mikael Karlsson.
Licensed under AGPLv3.
"""

import re
import pycountry


def map_language(language):
    if '_' in language:
        language = language.split('_')[0]
    if len(language) == 2:
        try: return pycountry.languages.get(alpha2=language.lower())
        except KeyError: pass
    elif len(language) == 3:
        try: return pycountry.languages.get(terminology=language.lower())
        except KeyError: pass
        try: return pycountry.languages.get(bibliographic=language.lower())
        except KeyError: pass
    else:
        try: return pycountry.languages.get(name=language.capitalize())
        except KeyError: pass
        try: return pycountry.languages.get(common_name=language.capitalize())
        except KeyError: pass
        for l in re.split('[,.;: ]+', language):
            try: return pycountry.languages.get(name=l.capitalize())
            except KeyError: pass
            try: return pycountry.languages.get(common_name=l.capitalize())
            except KeyError: pass

english = pycountry.languages.get(name='English')
chinese = pycountry.languages.get(name='Chinese')
arabic = pycountry.languages.get(name='Arabic')
bengali = pycountry.languages.get(alpha2='bn')

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

assert(map_language('bengali') is bengali)
assert(map_language('bangla') is bengali)

assert(map_language('zho') is chinese)
assert(map_language('chi') is chinese)

assert(map_language('Arabic, Moroccan Spoken') is arabic)


class language(object):
    def __init__(self, dash3, dash2b, dash2t, dash1, name):
        self.dash3 = dash3
        self.dash2b = dash2b
        self.dash2t = dash2t
        self.dash1 = dash1
        self.name = name


class iso639_3(object):
    def __init__(self):
        self.languages = [language(a, b, c, d, g) for a, b, c, d, e, f, g, h in self._fabtabular_py3()]
        self.dash3 = {x.dash3: x for x in self.languages}
        self.dash2b = {x.dash2b: x for x in self.languages if x.dash2b}
        self.dash2t = {x.dash2t: x for x in self.languages if x.dash3}
        self.dash1 = {x.dash1: x for x in self.languages if x.dash1}

    @staticmethod
    def _fabtabular_py3():
        import csv
        from urllib.request import urlopen
        import io

        with io.StringIO(urlopen('http://www-01.sil.org/iso639%2D3/iso-639-3.tab').read().decode()) as u:
            return list(csv.reader(u, delimiter='\t'))[1:]


i = iso639_3()
print(vars(i.languages[9]))
print(vars(i.dash3['ary']))
