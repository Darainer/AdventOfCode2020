input_file = "Day1input.txt"
#List_of_expenses = []
set_of_expenses = set()

with open(input_file, 'r') as file:
    for lines in file:
        l = lines.strip('\n')
        #List_of_expenses.append(int(l))
        set_of_expenses.add(int(l))

#List_of_expenses.sort()

#print("sorted list", List_of_expenses,  sep='\n')
Sum_value = 2020
#find the two numbers that add up to 2020 

# go through list from front
#find matching_second_expense
# search from back of second list



for expense in set_of_expenses:
    matching_second_expense = Sum_value - expense
    if matching_second_expense in set_of_expenses:
        answer = expense * matching_second_expense
        break

print(answer)

