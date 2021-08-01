from io import TextIOWrapper
import re


def parse_rules(text: TextIOWrapper) -> dict:
    rules_dict = dict()
    for line in text:
        line = line.strip('.\n')
        line = re.sub(r' [0-9] ', '', line)  # remove the bag numbers
        [bag_name, contents] = line.split(" bags contain")
        contents = contents.replace(" bags", "")
        contents = contents.replace(" bag", "")
        rules_dict[bag_name] = set(contents.split(","))
    return rules_dict


def Bag_wrapper_check(rules_dict: dict, target_bag: str) -> int:
    contains_target_bag = set()
    contains_target_bag.add(target_bag)
    previouslength = 0
    while(len(contains_target_bag) != previouslength):
        previouslength = len(contains_target_bag)
        # check all remaining bags for intersection with confirmed bags
        for rule in rules_dict:
            if (rules_dict[rule]).intersection(contains_target_bag):
                contains_target_bag.add(rule)
        # removing the known ones speeds up the remaining loops
        duplicates = contains_target_bag.intersection(rules_dict)      
        for duplicate in duplicates:
            del rules_dict[duplicate]
    return len(contains_target_bag)-1  # subtract the target bag


# input_file = "Day7_simpletest.txt"
input_file = "Day7_Input.txt"
target_bag = "shiny gold"
with open(input_file, 'r') as file:
    rules_dict = parse_rules(file)
    output = Bag_wrapper_check(rules_dict, target_bag)
    print(output)
