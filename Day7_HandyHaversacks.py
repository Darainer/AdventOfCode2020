
# rule parsing
# numbers can be ignored
# dictionary for each bag type
# stack for nested searching, stop when found target bag type of empty bag 

from io import TextIOWrapper
import re


def parse_rules(text: TextIOWrapper) -> dict:
    rules_dict = dict()
    for line in text:
        line = line.strip('.\n')
        line = re.sub(r' [0-9] ', '', line)  # remove the bag numbers because we dont need them
        [bag_name, contents] = line.split(" bags contain")
        contents = contents.replace(" bags", "")
        contents = contents.replace(" bag", "")
        content_list = contents.split(",")
        rules_dict[bag_name] = list(content_list)
        content_list.clear()
    return rules_dict


#input_file = "Day7_simpletest.txt"
input_file = "Day7_Input.txt"
with open(input_file, 'r') as file:
    parse_rules(file)
