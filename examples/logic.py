"""
Convert languages and language codes into ISO names

Copyright (c) 2014 Mikael Karlsson (CSC - IT Center for Science Ltd.).
Licensed under AGPLv3.
"""

import re

""" Use ISO 639-3 ?? """
dash3 = True

if dash3:
    languages = iso_639_3()
else:
    from pycountry import languages


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
