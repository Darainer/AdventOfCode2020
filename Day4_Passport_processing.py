input_file = 'Day4input.txt'
#input_file = 'Day4_simpletest.txt'

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

def isPassportDataValid(Passportdata: dict) -> bool:
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