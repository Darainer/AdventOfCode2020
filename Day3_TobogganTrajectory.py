input_file = 'Day3input.txt'
line_length = 31

def calculate_trees_hit( input_file, right_increment: int, vertical_increment: int ) -> int:
    row_position = 0
    number_of_trees = 0 
    row_count = 1
    with open(input_file, 'r') as file:
        for lines in file:
            row_count+=1
            if (row_count % vertical_increment != 1):
                l = lines.strip('\n')
                if(l[row_position] == '#'):
                    number_of_trees+=1
                row_position = (row_position + right_increment) % (line_length) 
    return number_of_trees      

#Part 1
Trees_right3_down1 = calculate_trees_hit(input_file,3, 1)
print("part 1 answer:",Trees_right3_down1)

#part2
slopes = [[3,1],[1,1], [5,1], [7,1], [1,2]]
part2_answer = 1
for slope_pair in slopes:
    part2_answer *= calculate_trees_hit(input_file,slope_pair[0], slope_pair[1])
print("part 2 answer:", part2_answer)
