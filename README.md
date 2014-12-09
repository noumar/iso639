# ISO639
ISO 639 library for Python.

## License
GNU Affero General Public License version 3 (AGPLv3)

## Supports
- ISO 639-1
- ISO 639-2
- ISO 639-3
- ISO 639-5

Doesn't support ISO 639-4 yet.

## Breaking changes
- 0.4.0: ```alpha3``` has been renamed to ```part3```. ```languages.alpha3``` might be used as an aggregation of all 'three letter codes' in the future.

## Compatibility
This library is aimed to be fully compatible with ```pycountry.languages```.

It provides the following attribute abstractions:

- ```terminology``` -> ```part2t```
- ```bibliographic``` -> ```part2b```
- ```alpha2``` -> ```part1```

If you have no intentions on using ```pycountry.languages``` or want/need to keep compatibility then please use the ```partX``` attributes for brevity and clarity.

## Installation
The package is pip installable from this repository. Future plans are to submit the package to PyPI.

### Latest stable
```
pip install git+https://github.com/noumar/iso639.git
```

### Specific version
```
pip install git+https://github.com/noumar/iso639.git@0.4.0
```

### Development branch
```
pip install git+https://github.com/noumar/iso639.git@development
```

## Upgrade
```pip list -o``` will not find updates. Use installation commands given above with ```-U``` flag.

## Development
```
git clone -b development https://github.com/noumar/iso639.git
pip install -e iso639
```

## Contains external data
- [ISO 639-3 Code Set](http://www-01.sil.org/iso639-3/iso-639-3.tab), dated 2014-03-20
- [ISO 639-3 Language Names Index](http://www-01.sil.org/iso639-3/iso-639-3_Name_Index.tab), dated 2014-03-20
- [ISO 639-3 Macrolanguage Mappings](http://www-01.sil.org/iso639-3/iso-639-3-macrolanguages.tab), dated 2014-03-20
- [ISO 639-3 Retired Code Element Mappings](http://www-01.sil.org/iso639-3/iso-639-3_Retirements.tab), dated 2014-03-20
- [ISO 639-1](http://id.loc.gov/vocabulary/iso639-1.tsv), on 2014-11-28
- [ISO 639-2](http://id.loc.gov/vocabulary/iso639-2.tsv), on 2014-11-28
- [ISO 639-5](http://id.loc.gov/vocabulary/iso639-5.tsv), dated 2011-05-12
