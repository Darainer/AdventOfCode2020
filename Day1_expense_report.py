input_file = "Day1input.txt"
List_of_expenses = []

with open(input_file, 'r') as file:
    for lines in file:
        l = lines.strip('\n')
        List_of_expenses.append(int(l))

List_of_expenses.sort()

print("sorted list", List_of_expenses,  sep='\n')
