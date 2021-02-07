input_file = "Day2input.txt"

# parsing rule
# min-max char: string
# 2-4 p: vpkpp

# todo: im missing using something like a cpp struct data structure here


def parsePasswordRule(line: str) -> [int, int, str]:
    [minmax, char_raw, string] = line.split()
    [minimum, maximum] = minmax.split("-")
    char = char_raw.split(":")
    return [int(minimum), int(maximum), char[0], string]


def checkPWcompliance_part1(PWRule: list) -> bool:
    numberchars_inPW = PWRule[3].count(PWRule[2])
    if PWRule[0] <= numberchars_inPW <= PWRule[1]:
        return True
    else:
        return False


def checkPWcompliance_part2(PWRule: list) -> bool:
    # xor first or second index of the string matches char
    if (PWRule[3][PWRule[0]-1] == PWRule[2]) ^ (PWRule[3][PWRule[1]-1] == PWRule[2]): 
        return True
    return False


CompliantPWs_part1 = 0  # count
CompliantPWs_part2 = 0  # count
with open(input_file, 'r') as file:
    for lines in file:
        PasswordRule = parsePasswordRule(lines)
        CompliantPWs_part1 += checkPWcompliance_part1(PasswordRule)
        CompliantPWs_part2 += checkPWcompliance_part2(PasswordRule)


print("number of part1 compliant PWs", CompliantPWs_part1)
print("number of part2 compliant PWs", CompliantPWs_part2)
