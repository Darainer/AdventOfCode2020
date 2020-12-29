input_file = 'Day3input.txt'
line_length = 31


def calculate_trees_hit( input_file, right_increment: int, vertical_increment: int ) -> int:
    row_position = 0
    number_of_trees = 0 
    row_count = 0
    with open(input_file, 'r') as file:
        for lines in file:
            row_count+=1
            if (row_count %vertical_increment == 0):
                l = lines.strip('\n')
                if(l[row_position] == '#'):
                    number_of_trees+=1
                row_position = (row_position + right_increment) % (line_length) 
    return number_of_trees      

#Part 1
Trees_right3_down1 = calculate_trees_hit(input_file,3, 1)
print(Trees_right3_down1)

#part2
Trees_right1_down1 = calculate_trees_hit(input_file,1, 1)
Trees_right5_down1 = calculate_trees_hit(input_file,5, 1)
Trees_right7_down1 = calculate_trees_hit(input_file,7, 1)
Trees_right1_down2 = calculate_trees_hit(input_file,1, 2)

answer = Trees_right1_down1*Trees_right3_down1*Trees_right5_down1*Trees_right7_down1*Trees_right1_down2
print(answer)