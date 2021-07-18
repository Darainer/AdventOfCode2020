from Day6_Custom_customs import Customs_checker, Count_group_common_answers


def test_Day6_exampleInputTest():
    input_file = "Day6_simpletest.txt"
    with open(input_file, 'r') as file:
        output_sum = Customs_checker(file)
    assert output_sum == 11


def test_Day6_part1InputTest():
    input_file = 'Day6_input.txt'
    with open(input_file, 'r') as file:
        output_sum = Customs_checker(file)
    print('day6 part a output = ', output_sum)
    assert output_sum == 6782


def test_Day6part2_exampleInputTest():
    input_file = "Day6_simpletest.txt"
    with open(input_file, 'r') as file:
        output_sum = Count_group_common_answers(file)
    assert output_sum == 6


def test_Day6part2_InputTest():
    input_file = "Day6_input.txt"
    with open(input_file, 'r') as file:
        output_sum = Count_group_common_answers(file)
    assert output_sum == 3596
