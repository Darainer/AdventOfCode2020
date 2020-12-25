input_file = "Day1input.txt"
set_of_expenses = set()

with open(input_file, 'r') as file:
    for lines in file:
        l = lines.strip('\n')
        set_of_expenses.add(int(l))

def find_matching_two_numbers(Sum_value :int, set_of_expenses: set) -> [int,int]:
    for expense in set_of_expenses:
        matching_remaining_expense = Sum_value - expense
        if matching_remaining_expense in set_of_expenses:
            answer = [expense, matching_remaining_expense]
            return answer   


#

#part 1: find the two numbers that add up to 2020 
# go through set
# for each member check if there exists a key which adds to 2020
Sum_value = 2020
answer = find_matching_two_numbers(2020,set_of_expenses)
print("part 1 answer = " , answer[0]*answer[1])

#part 2
# go through set
# for each member check if there exists a triplet where (member + sum(te) which adds to 2020




