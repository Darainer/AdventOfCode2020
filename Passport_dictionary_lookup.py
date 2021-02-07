valid_birth_year = r"^([1][9]\d\d|200[0-2])$"       # four digits; at least 1920 and at most 2002.
valid_issue_year = r"^([2][0][1]\d|2020)$"          # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
valid_ExpirationYear = r"^([2][0][2]\d|2030)$"      # eyr  - four digits; at least 2020 and at most 2030.
valid_height = r"^([1][5-8]\d[c][m]|[1][9][0-3][c][m]|59in|[6][0-9]in|[7][0-6]in)$" # a number followed by either cm or in:
                                                    # If cm, the number must be at least 150 and at most 193.
                                                    # If in, the number must be at least 59 and at most 76.
valid_hair_color = r"^(#[0-9a-f]{6})$"               # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
valid_eye_color = r"(^amb$|^blu$|^brn$|^gry$|^grn$|^hzl$|^oth$)" # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
valid_passportID = r"(^[0-9]{9}$)"                    # pid (Passport ID) - a nine-digit number, including leading zeroes.
valid_countryID = r"(.*)"                            # cid (Country ID) - ignored, missing or not.

ReferenceValueDictionary = dict(byr=valid_birth_year, iyr=valid_issue_year, eyr=valid_ExpirationYear, hgt=valid_height, hcl=valid_hair_color, ecl=valid_eye_color, pid=valid_passportID, cid=valid_countryID)

# added for readability
ReferenceFieldDictionary = dict(byr="Birth Year", iyr="Issue Year", eyr="Expiration Year", hgt="Height", hcl="Hair Color", ecl="Eye Color", pid="Passport ID", cid="Country ID")
