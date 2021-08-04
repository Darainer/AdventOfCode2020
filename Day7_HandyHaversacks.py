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


def parse_rules_with_count(text: TextIOWrapper) -> dict:
    rules_dict = dict()
    for line in text:
        line = line.strip('.\n')
        [bag_name, contents] = line.split(" bags contain")
        contents = contents.replace(" bags", "")
        contents = contents.replace(" bag", "")
        contents = contents.split(",")
        bag_type = []
        bag_count = []
        for bag_type_and_count in contents:
            if bag_type_and_count  != " no other":
                bag_count.append(int(bag_type_and_count[1]))
                bag_type.append(re.sub(r' [0-9] ', "", bag_type_and_count))
            rules_dict[bag_name] = [bag_type, bag_count]
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


def nested_bags_from_type(rules_with_count, target_bag) -> int:
    total_bags = int(0)
    [bags, counts] = rules_with_count[target_bag]
    for bag, count in zip(bags, counts):
        total_bags += count * (1 + nested_bags_from_type(rules_with_count, bag))
    return total_bags


def Part1_bags(input_file, target_bag) -> int:
    with open(input_file, 'r') as file:
        rules = parse_rules(file)
        count = Bag_wrapper_check(rules, target_bag)
    return count


def Part2_contents(input_file, target_bag) -> int:
    with open(input_file, 'r') as file:
        rules_with_count = parse_rules_with_count(file)
        total_bags = nested_bags_from_type(rules_with_count, target_bag)
    return total_bags
