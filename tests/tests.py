"""
Convert languages and language codes into ISO names

Copyright (c) 2014 Mikael Karlsson (CSC - IT Center for Science Ltd.).
Licensed under AGPLv3.
"""

import unittest

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

    def test_logic_2_char_code(self):
        self.assertIs(map_language('En'), self.english)
        self.assertIs(map_language('EN'), self.english)
        self.assertIs(map_language('eN'), self.english)
        self.assertIs(map_language('en'), self.english)

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

    def test_logic_locale(self):
        self.assertIs(map_language('En_Us'), self.english)
        self.assertIs(map_language('EN_US'), self.english)
        self.assertIs(map_language('en_us'), self.english)

    def test_logic_dash3(self):
        self.assertIs(map_language('ary'), self.moroccan)
        self.assertIs(languages.alpha3['ary'], self.moroccan)
        self.assertIs(languages.get(alpha3='ary'), self.moroccan)
        self.assertIs(map_language('Moroccan Arabic'), self.moroccan)
        self.assertIs(map_language('Tzeltal'), self.tzeltal)
        self.assertIs(map_language('Tzeltal, Tenejapa'), self.tzeltal)
        self.assertIs(map_language('tzh'), self.tzeltal)

    def test_logic_dash2(self):
        self.assertEqual(map_language('Moroccan Arabic', False).name, 'Arabic')

if __name__ == '__main__':
    unittest.main()
