"""
Python library for ISO 639 standard

Copyright (c) 2014 Mikael Karlsson (CSC - IT Center for Science Ltd.).
Licensed under AGPLv3.
"""

import re


def map_language(language, dash3=True):
    """ Use ISO 639-3 ?? """
    if dash3:
        from iso639 import languages
    else:
        from pycountry import languages

    if '_' in language:
        language = language.split('_')[0]
    if len(language) == 2:
        try: return languages.get(alpha2=language.lower())
        except KeyError: pass
    elif len(language) == 3:
        if dash3:
            try: return languages.get(part3=language.lower())
            except KeyError: pass
        try: return languages.get(terminology=language.lower())
        except KeyError: pass
        try: return languages.get(bibliographic=language.lower())
        except KeyError: pass
    else:
        try: return languages.get(name=language.title())
        except KeyError: pass
        if dash3:
            try: return languages.get(inverted=language.title())
            except KeyError: pass
        for l in re.split('[,.;: ]+', language):
            try: return languages.get(name=l.title())
            except KeyError: pass
