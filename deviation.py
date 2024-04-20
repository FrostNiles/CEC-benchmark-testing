import numpy as np
import sys

argNum = sys.argv[1]

# Read the original numbers
with open(f'input_data/shift_data_{argNum}.txt', 'r') as file:
    original_data = file.read()

# Read the new numbers
with open(f'test_data/shift_data_{argNum}.txt', 'r') as file:
    new_data = file.read()

# Split the data into individual numbers
original_numbers = [float(i) for i in original_data.split()]
new_numbers = [float(i) for i in new_data.split()]

# Get n from command line arguments
n = int(sys.argv[2])

# Calculate the deviations for the first n numbers
deviations = [abs(original - new) for original, new in zip(original_numbers[:n], new_numbers[:n])]

average_deviation = sum(deviations) / len(deviations)
print("Average deviation: ", average_deviation)

median_deviation = np.median(deviations)

print("Median deviation: ", median_deviation)

with open(f'test_data/shift_data_{argNum}_deviation_final.txt', 'w') as file:
    file.write(f"{median_deviation:.5e}")