"""
Python library for ISO 639 standard

Copyright (c) 2014 Mikael Karlsson (CSC - IT Center for Science Ltd.).
Licensed under AGPLv3.
"""

import sys
import collections
if sys.version_info[0:2] == (2, 6):
    import unittest2 as unittest
else:
    import unittest

from iso639 import Iso639, languages
from examples.logic import map_language


class ClassFunctionality(unittest.TestCase):
    """
    Test cases for library class implementation
    """
    def test_singleton(self):
        self.assertIs(Iso639(), Iso639())
        self.assertIs(Iso639().alpha2['en'], Iso639().alpha2['en'])

    def test_2_char_code(self):
        self.assertEqual(languages.get(alpha2='en').name, 'English')
        self.assertEqual(languages.alpha2['en'].name, 'English')

    def test_bibliographic(self):
        self.assertEqual(languages.get(bibliographic='dut').name, 'Dutch')
        self.assertEqual(languages.bibliographic['dut'].name, 'Dutch')

    def test_terminology(self):
        self.assertEqual(languages.get(terminology='nld').name, 'Dutch')
        self.assertEqual(languages.terminology['nld'].name, 'Dutch')

    def test_3_char_code(self):
        self.assertEqual(languages.get(alpha3='eng').name, 'English')
        self.assertEqual(languages.alpha3['eng'].name, 'English')

    def test_retired_code(self):
        # TODO: self.assertEqual(languages.get(alpha3='ron').retired, 'mol')
        self.assertEqual(languages.get(retired='mol'), languages.get(alpha3='ron'))
        self.assertEqual(languages.retired['mol'], languages.alpha3['ron'])
        self.assertIsInstance(languages.get(retired='nlr'), str)
        self.assertIsInstance(languages.retired['nlr'], str)

    def test_name(self):
        self.assertEqual(languages.get(name='English').alpha3, 'eng')
        self.assertEqual(languages.name['English'].alpha3, 'eng')

    def test_macro_name(self):
        # TODO: self.assertEqual(languages.get(name='Standard Estonian').macro, languages.get(alpha3='est'))
        self.assertEqual(languages.get(name='Standard Estonian').macro, 'est')

    def test_inverted(self):
        self.assertEqual(languages.get(inverted='Arabic, Moroccan').name, 'Moroccan Arabic')
        self.assertEqual(languages.inverted['Arabic, Moroccan'].name, 'Moroccan Arabic')

    def test_property_lengths(self):
        self.assertEqual(len(languages.languages), 7879)
        self.assertEqual(len(languages.name), 7879)
        self.assertEqual(len(languages.alpha2), 184)
        self.assertEqual(len(languages.bibliographic), 418)
        self.assertEqual(len(languages.terminology), 418)
        self.assertEqual(len(languages.alpha3), 7879)
        self.assertEqual(len(languages.inverted), 7879)
        self.assertEqual(len(languages.macro), 62)
        self.assertEqual(len(languages.retired), 243)

    def test_len(self):
        self.assertIsInstance(len(languages), int)
        self.assertEqual(len(languages), 7879)

    def test_iter(self):
        self.assertIsInstance(languages, collections.Iterable)
        self.assertIsInstance(iter(languages), collections.Iterator)

    def test_exceptions(self):
        self.assertRaises(KeyError, languages.get, alpha2='En')
        self.assertRaises(KeyError, languages.get, name='Moroccan')
        self.assertRaises(AttributeError, languages.get, alpha1='en')
        self.assertRaises(AttributeError, languages.get, alpha2='en', name='English')


class LogicFunctionality(unittest.TestCase):
    """
    Test cases for example logic implementation
    """
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
