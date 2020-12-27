input_file = "Day2input.txt"

# parsing rule
# min-max char: string
# 2-4 p: vpkpp

#todo: im missing using something like a cpp struct data structure here

def parsePasswordRule(line: str) -> [int , int , str]:
    [minmax, char_raw, string] = line.split()
    [minimum, maximum] = minmax.split("-")
    char = char_raw.split(":")
    return [int(minimum),int(maximum),char[0],string]

def checkPWcompliance(PWRule : list) -> bool:  #min_char: int, max_char: int, char: str) -> bool:
    numberchars_inPW = PWRule[3].count(PWRule[2])
    if PWRule[0] <= numberchars_inPW <= PWRule[1]:
        return True
    else:
        return False

CompliantPWs = 0 #count

with open(input_file, 'r') as file:
    for lines in file:
        PasswordRule = parsePasswordRule(lines) 
        CompliantPWs += checkPWcompliance(PasswordRule)

print("number of compliant PWs", CompliantPWs)