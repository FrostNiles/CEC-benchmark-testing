import re
import sys

argNum = sys.argv[1]

# Open the file and read its contents
with open(f'test_data/shift_data_{argNum}_upper.txt', 'r') as file:
    upper = file.read()

# open the latest backup file and read its contents
with open(f'test_data/shift_data_{argNum}_lower.txt', 'r') as file:
    lower = file.read()

#backup the data to the step backup

lower_numbers = [float(i) for i in lower.split()]
upper_numbers = [float(i) for i in upper.split()]

#print("lower_numbers", lower_numbers[0])
#print("upper_numbers", upper_numbers[0])


# now I want to bisecting the interval between the two numbers on the same position in each file
# I want to get the number in the middle between the two numbers with bisecting the interval

middle_numbers = [(upper_numbers[i] + lower_numbers[i]) / 2 for i in range(len(upper_numbers))]
#print("middle_numbers", middle_numbers[0])

# now I want to write the middle numbers to the original file just the number and with a space behind the number
with open(f'test_data/shift_data_{argNum}.txt', 'w') as file:
    for number in middle_numbers:
        file.write(f"{number} ")


