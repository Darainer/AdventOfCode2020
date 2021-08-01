
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
        rules_dict[bag_name] = set(contents.split(","))
    return rules_dict


def Bag_wrapper_check(rules_dict: dict, target_bag: str) ->bool:
    contains_target_bag = set()
    contains_target_bag.add(target_bag)
    previouslength = 0
    while(len(contains_target_bag) == previouslength):
        for rule in rules_dict:
            if (rules_dict[rule]).intersection(contains_target_bag):
                contains_target_bag.add(rule)
        previouslength= len(contains_target_bag)
    return len(contains_target_bag)-1

#input_file = "Day7_simpletest.txt"
input_file = "Day7_Input.txt"
target_bag = "shiny gold"
with open(input_file, 'r') as file:
    rules_dict = parse_rules(file)
    output = Bag_wrapper_check(rules_dict,target_bag)
    print(output)
