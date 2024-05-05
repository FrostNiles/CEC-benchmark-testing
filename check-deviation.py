import sys
import runpy

argNum = sys.argv[1]
dimension = sys.argv[2]
number_of_element = int(sys.argv[3]) - 1


# Read the original numbers
with open(f'input_data/shift_data_{argNum}.txt', 'r') as file:
    original_data = file.read()

# read the deviation


with open(f'test_data/result/result_data_{argNum}_dim_{dimension}_number_of_element_{number_of_element+1}.txt', 'r') as file:
    data = file.read()

# Extract the numbers from the lines
data = data.split('deviation:')
deviation = float(data[1])
print("deviation", deviation)

# now delete from the original data on the number_of_element position the deviation
original_numbers = [float(i) for i in original_data.split()]

original_numbers[number_of_element] = original_numbers[number_of_element] - deviation

with open(f'test_data/shift_data_{argNum}_dim_{dimension}_element_{number_of_element+1}.txt', 'w') as file:
    for number in original_numbers:
        file.write(f"{number} ")

# run the main program
runpy.run_path('./run-main.py')