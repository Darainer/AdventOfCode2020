import numpy as np
input_file = 'Day5input.txt'


def ParseBoardingPass(raw_row: str, raw_col: str) -> [int, int]:
    bin_row = raw_row.replace("F", "0").replace("B", "1")
    row = int(bin_row, 2)
    bin_col = raw_col.replace("L", "0").replace("R", "1")
    col = int(bin_col, 2)
    return [row, col]


all_seats = np.zeros((128, 8))
with open(input_file, 'r') as file:
    highestSeatID = 0
    for line in file:
        [row, column] = ParseBoardingPass(line[0:7], line[7:10])  # second slicing element is exclusive
        seatID = row*8 + column
        all_seats[row, column] = 1
        highestSeatID = max(highestSeatID, seatID)

print(highestSeatID)  # part1
print(all_seats)  # part2: seat Map of plane
