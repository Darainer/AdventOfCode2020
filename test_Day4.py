import re
# import pytest
from Passport_dictionary_lookup import ReferenceValueDictionary


def test_birth_year_regex():
    years = ["103", "1900", "1980", "1999", "2003", "2010", "2020", "2021", "2099"]
    results = []
    for year in years:
        result = re.search(ReferenceValueDictionary["byr"], year)
        results.append(bool(result))
        print(year, " : ", result)
    assert results == [0, 1, 1, 1, 0, 0, 0, 0, 0]


def test_height_cm_regex():
    heights = ["120cm", "156cm", "198cm"]
    results = []
    for height in heights:
        result = re.search(ReferenceValueDictionary["hgt"], height)
        results.append(bool(result))
        # print(height, " : ", result)
    assert results == [0, 1, 0]


def test_height_in_regex():
    heights_in = ["44in", "58in", "59in", "63in", "75in", "98in"]
    results = []
    for height in heights_in:
        result = re.search(ReferenceValueDictionary["hgt"], height)
        results.append(bool(result))
        # print(height, " : ", result)
    assert results == [0, 0, 1, 1, 1, 0]
