import re
input_file = 'Day4input.txt'
#input_file = 'Day4_simpletest.txt'

valid_birth_year = r"^([1][9]\d\d|200[0-2])$"       # four digits; at least 1920 and at most 2002.
valid_issue_year = r"^([2][0][1]\d|2020)$"          #iyr (Issue Year) - four digits; at least 2010 and at most 2020.
valid_ExpirationYear = r"^([2][0][2]\d|2030)$"      #eyr  - four digits; at least 2020 and at most 2030.
valid_height = r"([1][5-8]\d[c][m]|[1][9][0-3][c][m]|59in|[6][0-9]in|[7][0-6]in)" # a number followed by either cm or in:
                                                    #If cm, the number must be at least 150 and at most 193.
                                                    #If in, the number must be at least 59 and at most 76.
valid_hair_color = r"(a[0-9a-f]{6})"               #hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
valid_eye_color = r"(amb|blu|brn|gry|grn|hzl|oth)" # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
valid_passportID = r"([0-9]{6})"                     #pid (Passport ID) - a nine-digit number, including leading zeroes.
#cid (Country ID) - ignored, missing or not.

ReferenceValueDictionary = dict(byr=valid_birth_year,iyr=valid_issue_year,eyr=valid_ExpirationYear,hgt=valid_height,hcr=valid_hair_color, ecl=valid_eye_color,pid=valid_passportID)

#added for readability
ReferenceFieldDictionary= dict(byr="Birth Year", iyr ="Issue Year", eyr="Expiration Year",hgt="Height", hcl="Hair Color",ecl="Eye Color", pid="Passport ID",cid="Country ID")



def ParsePassportData(currentPassport: list) -> dict:
    PassportDictionary= dict(isValid=True)
    for line in currentPassport:
        entries = line.split(' ')
        for entry in entries:
            [key, value] = entry.split(":")
            try:
                FieldName = ReferenceFieldDictionary[key]
                PassportDictionary[FieldName]= value
            except:
                PassportDictionary[isValid]=False
                return PassportDictionary
    return PassportDictionary

def isPassportValueValid(Passportdata : dict ,field_for_test : str) -> bool:
    if field_for_test[0] == 'byr':    #need tests for all strings
        value_test = ReferenceValueDictionary[field_for_test[0]]
        result = re.search(value_test,Passportdata[field_for_test[1]])
    return result

def isPassportDataValid(Passportdata: dict) -> bool:
    for  requiredfields in ReferenceFieldDictionary.items():
        if requiredfields[1] not in Passportdata.keys():
            if requiredfields[1] != "Country ID":  #is optional for North pole passports
                print("invalid Passport: missing",requiredfields[1])
                return False
        if not isPassportValueValid(Passportdata,requiredfields):
            print("invalid value in field", requiredfields[1])
            return False 
    return True

#init
ValidPassportCounter = 0
currentPassport_rawinput= []
PassportDictionary = dict()

with open(input_file, 'r') as file:
    for line in file:
        if line == '\n':
            #processPassport
            PassportDictionary = ParsePassportData(currentPassport_rawinput)
            ValidPassportCounter += isPassportDataValid(PassportDictionary)
            currentPassport_rawinput.clear()
            continue
        l = line.strip('\n')
        currentPassport_rawinput.append(l)

print(ValidPassportCounter)