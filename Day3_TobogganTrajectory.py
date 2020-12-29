input_file = 'Day3input.txt'


right_increment = 3
row_position = 0
number_of_trees = 0 

with open(input_file, 'r') as file:
    line = file.readline().strip('\n')
    line_length = len(line)
    for lines in file:
        l = lines.strip('\n')
        if(l[row_position] == '#'):
            number_of_trees+=1
        row_position = (row_position + 3) % line_length    
        
print(number_of_trees)        