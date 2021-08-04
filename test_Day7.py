from Day7_HandyHaversacks import parse_rules, Part1_bags, Part2_contents, parse_rules_with_count


def test_Day7_exampleInputParserTest():
    input_file = "Day7_simpletest.txt"
    with open(input_file, 'r') as file:
        output_sum = parse_rules(file)
    assert output_sum['shiny gold'] == {'vibrant plum', 'dark olive'}


def test_part1():
    input_file = "Day7_Input.txt"
    target_bag = "shiny gold"
    output = Part1_bags(input_file, target_bag)
    assert output == 268


def test_Day7_part2_exampleParserTest_with_count():
    input_file = "Day7_simpletest.txt"
    with open(input_file, 'r') as file:
        output_rules = parse_rules_with_count(file)
    assert output_rules["shiny gold"] == [['dark olive', 'vibrant plum'], [1, 2]]


def test_Day7_part2():
    input_file = "Day7_Input.txt"
    target_bag = "shiny gold"
    output = Part2_contents(input_file, target_bag)
    assert output == 7867
