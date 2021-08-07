from Day1_expense_report import find_matching_two_numbers, find_matching_three_numbers, parse_expenses

sum_value = 2020
input_file = "Day1input.txt"


# part 1: find the two numbers that add up to the sum
def test_part1():
    set_of_expenses = parse_expenses(input_file)
    answer = find_matching_two_numbers(sum_value, set_of_expenses)
    assert answer[0]*answer[1] == 800139


# part 2: for each member check for a triplet where member + sum(te) = 2020
def test_part2():
    set_of_expenses = parse_expenses(input_file)
    answer2 = find_matching_three_numbers(2020, set_of_expenses)
    assert answer2[0]*answer2[1]*answer2[2] == 59885340
