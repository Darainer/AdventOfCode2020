import re
from Passport_dictionary_lookup import ReferenceValueDictionary, ReferenceFieldDictionary
input_file = 'Day4input.txt'
# input_file = 'Day4_simpletest.txt'


def ParsePassportData(currentRawPassport: list) -> dict:
    PassportDictionary = dict(isValid=True)
    for line in currentRawPassport:
        entries = line.split(' ')
        for entry in entries:
            [key, value] = entry.split(":")
            if key in ReferenceFieldDictionary:  # check if key is valid
                PassportDictionary[key] = value
            else:
                PassportDictionary[isValid] = False
    return PassportDictionary


def isPassportValueValid(Passportdata: dict, field_for_test: str) -> bool:
    if field_for_test[0] == "cid":
        return True     # not testing it, valid passport may or may not contain it
    else:
        value_test = ReferenceValueDictionary[field_for_test[0]]
        result = re.search(value_test, Passportdata[field_for_test[0]])
        if result:
            return True
        else:
            return False


def isPassportDataValid(Passportdata: dict) -> bool:
    for requiredfields in ReferenceFieldDictionary.items():
        if requiredfields[0] not in Passportdata.keys():
            if requiredfields[1] != "Country ID":  # is optional for North pole passports
                print("invalid Passport: missing", requiredfields[1])
                return False
        if not isPassportValueValid(Passportdata, requiredfields):
            print("invalid value in field : ", requiredfields[1])
            return False
    return True


# init
ValidPassportCounter = 0
currentPassport_rawinput = []
PassportDictionary = dict()

with open(input_file, 'r') as file:
    for line in file:
        if line == '\n':  # we reached the end of a single passport
            # processPassport
            PassportDictionary = ParsePassportData(currentPassport_rawinput)
            ValidPassportCounter += isPassportDataValid(PassportDictionary)
            currentPassport_rawinput.clear()
            continue
        currentPassport_rawinput.append(line.strip('\n'))

print(ValidPassportCounter)
