import sys

argNum = sys.argv[1]
# Read the original numbers
with open(f'input_data/shift_data_{argNum}.txt', 'r') as file:
    original_data = file.read()

# Read the new numbers

# Split the data into individual numbers
original_numbers = [float(i) for i in original_data.split()]

with open(f'test_data/shift_data_{argNum}_deviation_final.txt', 'r') as file:
    median_deviation = float(file.read())
print("Median deviation: ", median_deviation)
#median_deviation = 7.10541e-15
#3.552713678800501e-15
# Add the median deviation to the original numbers
adjusted_numbers = [original - median_deviation for original in original_numbers]

# Write the adjusted numbers to a new file

with open(f'test_data/shift_data_{argNum}.txt', 'w') as file:
    for number in adjusted_numbers:
        file.write(f"{number} ")