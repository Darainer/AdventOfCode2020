input_file = 'Day3input.txt'


right_increment = 3
row_position = 0
number_of_trees = 0 

with open(input_file, 'r') as file:
    for lines in file:
        l = lines.strip('\n')
        if row_position > len(l)-1:
            break
        if(l[row_position] == '#'):
            number_of_trees+=1
        row_position+=right_increment
        

print(number_of_trees)        