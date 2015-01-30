"""
Python library for ISO 639 standard

Copyright (c) 2014-2015 Mikael Karlsson (CSC - IT Center for Science Ltd.).
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
from pycountry import languages as pclanguages


class ClassFunctionality(unittest.TestCase):
    """
    Test cases for library class implementation
    """
    def test_singleton(self):
        self.assertIs(Iso639(), Iso639())
        self.assertIs(Iso639().part1['en'], Iso639().part1['en'])

    def test_part1(self):
        self.assertEqual(languages.get(part1='en').name, 'English')
        self.assertEqual(languages.part1['en'].name, 'English')

    def test_part2b(self):
        self.assertEqual(languages.get(part2b='dut').name, 'Dutch')
        self.assertEqual(languages.part2b['dut'].name, 'Dutch')

    def test_part2t(self):
        self.assertEqual(languages.get(part2t='nld').name, 'Dutch')
        self.assertEqual(languages.part2t['nld'].name, 'Dutch')

    def test_part3(self):
        self.assertEqual(languages.get(part3='eng').name, 'English')
        self.assertEqual(languages.part3['eng'].name, 'English')

    def test_retired_code(self):
        # TODO: self.assertEqual(languages.get(alpha3='ron').retired, 'mol')
        self.assertEqual(languages.get(retired='mol'), languages.get(part3='ron'))
        self.assertEqual(languages.retired['mol'], languages.part3['ron'])
        self.assertIsInstance(languages.get(retired='nlr'), str)
        self.assertIsInstance(languages.retired['nlr'], str)
        self.assertEqual(languages.get(retired='sh'), languages.get(part3='hbs'))
        self.assertEqual(languages.retired['sh'], languages.part3['hbs'])

    def test_name(self):
        self.assertEqual(languages.get(name='English').part3, 'eng')
        self.assertEqual(languages.name['English'].part3, 'eng')

    def test_alternative_name(self):
        self.assertEqual(languages.get(name='Romanian').part3, 'ron')
        self.assertEqual(languages.get(name='Moldavian').part3, 'ron')
        self.assertEqual(languages.get(name='Moldovan').part3, 'ron')

        self.assertEqual(languages.get(name='Dimili').part3, 'zza')
        self.assertEqual(languages.get(name='Dimli (macrolanguage)').part3, 'zza')
        self.assertEqual(languages.get(name='Kirdki').part3, 'zza')
        self.assertEqual(languages.get(name='Kirmanjki (macrolanguage)').part3, 'zza')
        self.assertEqual(languages.get(name='Zaza').part3, 'zza')
        self.assertEqual(languages.get(name='Zazaki').part3, 'zza')

    def test_macro_name(self):
        # TODO: self.assertEqual(languages.get(name='Standard Estonian').macro, languages.get(alpha3='est'))
        self.assertEqual(languages.get(name='Standard Estonian').macro, 'est')

    def test_collective_name(self):
        self.assertEqual(languages.get(name='Bihari languages').part2b, 'bih')
        self.assertEqual(languages.get(name='Sami languages').part2b, 'smi')
        self.assertEqual(languages.get(name='Bihari languages').part5, 'bih')
        self.assertEqual(languages.get(name='Sami languages').part5, 'smi')

    def test_inverted(self):
        self.assertEqual(languages.get(inverted='Arabic, Moroccan').name, 'Moroccan Arabic')
        self.assertEqual(languages.inverted['Arabic, Moroccan'].name, 'Moroccan Arabic')

    def test_property_lengths(self):
        self.assertEqual(len(languages.languages), 7979)
        self.assertEqual(len(languages.name), 8254)
        self.assertEqual(len(languages.part1), 184)
        self.assertEqual(len(languages.part2b), 485)
        self.assertEqual(len(languages.part2t), 485)
        self.assertEqual(len(languages.part3), 7863)
        self.assertEqual(len(languages.part5), 115)
        self.assertEqual(len(languages.inverted), 7862)
        self.assertEqual(len(languages.macro), 62)
        self.assertEqual(len(languages.retired), 271)

    def test_len(self):
        self.assertIsInstance(len(languages), int)
        self.assertEqual(len(languages), 7979)

    def test_iter(self):
        self.assertIsInstance(languages, collections.Iterable)
        self.assertIsInstance(iter(languages), collections.Iterator)

    def test_exceptions(self):
        self.assertRaises(KeyError, languages.get, part1='En')  # Wrong value
        self.assertRaises(KeyError, languages.get, name='Moroccan')  # Wrong value
        self.assertRaises(AttributeError, languages.get, alpha1='en')  # Wrong keyword
        self.assertRaises(AttributeError, languages.get, part1='en', name='English')  # Too many keywords


class CompatibilityChecks(unittest.TestCase):
    """
    Test cases for library class compatibility against pycountry.languages
    """
    @classmethod
    def setUpClass(cls):
        cls.pcterm = set(pclanguages.indices['terminology'].keys())
        cls.term = set(languages.terminology.keys())
        cls.pcbib = set(pclanguages.indices['bibliographic'].keys())
        cls.bib = set(languages.bibliographic.keys())
        cls.pcalpha2 = set(pclanguages.indices['alpha2'].keys())
        cls.alpha2 = set(languages.alpha2.keys())

        # Retired or invalid codes
        cls.pcterm -= set(['mol', 'qaa-qtz'])
        cls.pcbib -= set(['mol', 'qaa-qtz'])
        cls.pcalpha2 -= set(['mo'])

    def test_compare_bibliographic(self):
        self.assertEqual(self.bib, self.pcbib)

    def test_compare_terminology(self):
        self.assertEqual(self.term, self.pcterm)

    def test_compare_alpha2(self):
        self.assertEqual(self.alpha2, self.pcalpha2)


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

    def test_logic_part3(self):
        self.assertIs(map_language('ary'), self.moroccan)
        self.assertIs(languages.part3['ary'], self.moroccan)
        self.assertIs(languages.get(part3='ary'), self.moroccan)
        self.assertIs(map_language('Moroccan Arabic'), self.moroccan)
        self.assertIs(map_language('Tzeltal'), self.tzeltal)
        self.assertIs(map_language('Tzeltal, Tenejapa'), self.tzeltal)
        self.assertIs(map_language('tzh'), self.tzeltal)

    def test_logic_part2(self):
        self.assertEqual(map_language('Moroccan Arabic', False).name, 'Arabic')


if __name__ == '__main__':
    unittest.main()
