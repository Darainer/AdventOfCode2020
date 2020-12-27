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
    return [0,0]

def find_matching_three_numbers(Sum_value :int, set_of_expenses: set) -> [int,int,int]:
    for expense1 in set_of_expenses:
        matching_remaining_expense = Sum_value - expense1
        for expense2 in set_of_expenses:
            if expense1 != expense2:
                answer = find_matching_two_numbers(matching_remaining_expense,set_of_expenses)
                if answer[0] != 0:
                    return [expense1, answer[0], answer[1]]
  
#part 1: find the two numbers that add up to 2020 
# go through set
# for each member check if there exists a key which adds to 2020
Sum_value = 2020
answer = find_matching_two_numbers(2020,set_of_expenses)
print("part 1 answer = " , answer[0]*answer[1])

#part 2
# go through set
# for each member check if there exists a triplet where (member + sum(te) which adds to 2020
sum_value = 2020
answer2 = find_matching_three_numbers(2020, set_of_expenses)
print("numbers that add to 2020", answer2[0], answer2[1], answer2[2])
print( "part 2 answer = ", answer2[0]*answer2[1]*answer2[2])


