from Day7_HandyHaversacks import parse_rules


def test_Day6_exampleInputTest():
    input_file = "Day7_simpletest.txt"
    with open(input_file, 'r') as file:
        output_sum = parse_rules(file)
    assert output_sum == dict()
