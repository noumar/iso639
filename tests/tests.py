from iso_639_3 import map_language, iso_639_3

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
