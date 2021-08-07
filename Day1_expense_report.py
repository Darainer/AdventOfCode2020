def parse_expenses(input_file):
    set_of_expenses = set()
    with open(input_file, 'r') as file:
        for lines in file:
            line = lines.strip('\n')
            set_of_expenses.add(int(line))
    return set_of_expenses


def find_matching_two_numbers(Sum_value: int, set_of_expenses: set) -> list:
    for expense in set_of_expenses:
        matching_remaining_expense = Sum_value - expense
        if matching_remaining_expense in set_of_expenses:
            answer = [expense, matching_remaining_expense]
            return answer
    return [0, 0]


def find_matching_three_numbers(Sum_value: int, set_of_expenses: set) -> list:
    for expense1 in set_of_expenses:
        matching_remaining_expense = Sum_value - expense1
        for expense2 in set_of_expenses:
            if expense1 != expense2:
                answer = find_matching_two_numbers(matching_remaining_expense, set_of_expenses)
                if answer[0] != 0:
                    return [expense1, answer[0], answer[1]]
