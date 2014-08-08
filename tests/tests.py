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

    def test_logic_3_char_code(self):
        self.assertIs(map_language('Eng'), self.english)
        self.assertIs(map_language('eNg'), self.english)
        self.assertIs(map_language('enG'), self.english)
        self.assertIs(map_language('ENG'), self.english)
        self.assertIs(map_language('eng'), self.english)
        self.assertIs(map_language('zho'), self.chinese)
        self.assertIs(map_language('chi'), self.chinese)
        self.assertIs(map_language('ara'), self.arabic)

    def test_logic_name(self):
        self.assertIs(map_language('english'), self.english)
        self.assertIs(map_language('English'), self.english)
        self.assertIs(map_language('eNgLiSh'), self.english)
        self.assertIs(map_language('ENGLISH'), self.english)
        self.assertIs(map_language('Arabic, Moroccan'), self.moroccan)
        self.assertIs(map_language('Arabic, Moroccan Spoken'), self.arabic)

assert(map_language('En') is english)
assert(map_language('EN') is english)
assert(map_language('eN') is english)
assert(map_language('en') is english)
assert(map_language('En_Us') is english)
assert(map_language('EN_US') is english)
assert(map_language('en_us') is english)

if dash3:
    assert(map_language('ary') is moroccan)
    assert(languages.alpha3['ary'] is moroccan)
    assert(languages.get(alpha3='ary') is moroccan)
    assert(map_language('Moroccan Arabic') is moroccan)
    assert(map_language('Tzeltal') is tzeltal)
    assert(map_language('tzh') is tzeltal)
else:
    assert(map_language('Moroccan Arabic') is arabic)
