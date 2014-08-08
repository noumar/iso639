"""
Convert languages and language codes into ISO names

Copyright (c) 2014 Mikael Karlsson (CSC - IT Center for Science Ltd.).
Licensed under AGPLv3.
"""

from iso_639_3 import iso_639_3, languages
from examples.logic import map_language

class LogicFunctionality(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.english = languages.get(name='English')
        cls.chinese = languages.get(name='Chinese')
        cls.arabic = languages.get(name='Arabic')
        cls.moroccan = languages.get(name='Moroccan Arabic')
        cls.tzeltal = languages.get(name='Tzeltal')


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
    assert(map_language('ary') is moroccan)
    assert(languages.alpha3['ary'] is moroccan)
    assert(languages.get(alpha3='ary') is moroccan)
    assert(map_language('Moroccan Arabic') is moroccan)
    assert(map_language('Tzeltal') is tzeltal)
    assert(map_language('tzh') is tzeltal)
else:
    assert(map_language('Moroccan Arabic') is arabic)
