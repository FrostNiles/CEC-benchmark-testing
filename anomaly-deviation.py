import sys
import runpy
import re
# Read the numbers from the file
argNum = sys.argv[1]
dimension = sys.argv[2]
number_of_element = int(sys.argv[3]) - 1

with open(f'test_data/result/result_data_{argNum}_dim_{dimension}_number_of_element_{number_of_element+1}.txt', 'r') as file:
    lines = file.readlines()
print("lines", lines)
if len(lines) < 3:
    sys.exit()
# Extract the numbers from the lines
number1 = float(lines[1])
number2 = float(lines[2])

# Calculate the deviation
deviation = abs(number1 - number2)
print("deviation", deviation)
deviation = str(deviation)
#deviation = 4.881784197001252e-16 
with open(f'test_data/result/result_data_{argNum}_dim_{dimension}_number_of_element_{number_of_element+1}.txt', 'w') as file:
            file.write("deviation:")
            file.write(deviation)

#now I want to test the deviation with the original data
# Read the original numbers

with open(f'input_data/shift_data_{argNum}.txt', 'r') as file:
    original_data = file.read()

original_numbers = [float(i) for i in original_data.split()]

original_numbers[number_of_element] = original_numbers[number_of_element] - deviation

with open(f'test_data/shift_data_{argNum}.txt', 'w') as file:
    for number in original_numbers:
        file.write(f"{number} ")


runpy.run_path('./run-main.py')

with open(f'test_data/current_result_{argNum}.txt', 'r') as file:
    result = file.read()

# Find the number in the string
result = re.findall(r'\d+\.\d+', result)

# Convert to float when you need to do a numerical operation

result = str(result)
result = result.split('.')
#before the floating point
before = result[0]
#after the floating point
after = result[1]

# Now I want to get the first 8 digits from after
sevenDigits = after[:7]
#this is how the ["['3000", "0000000053']"] looks like
#I want to get the last two digits from the after
# and im getting  "']" so I need to get the last two digits from the after
lastTwoDigits = after.split('\'')[0][-2:]
lastDeviation = str(deviation)

#import original data from input_data/shift_data_{argNum}.txt
with open(f'input_data/shift_data_{argNum}.txt', 'r') as file:
     full_data = file.read()

full_data_numbers = [float(i) for i in full_data.split()]


if int(sevenDigits) > 0:

    while int(sevenDigits) != 0:


        original_numbers[number_of_element] = (original_numbers[number_of_element] + full_data_numbers[number_of_element])/2

        with open(f'test_data/shift_data_{argNum}.txt', 'w') as file:
            for number in original_numbers:
                file.write(f"{number} ")


        runpy.run_path('./run-main.py')

        #count deviation in the exact position
        #deviation = abs(original_numbers[number_of_element] - full_data_numbers[number_of_element])
        print("deviation", deviation)

        with open(f'test_data/current_result_{argNum}.txt', 'r') as file:
            result = file.read()

        # Find the number in the string
        result = re.findall(r'\d+\.\d+', result)

        result = str(result)
        result = result.split('.')
        #before the floating point
        before = result[0]
        #after the floating point
        after = result[1]

        # Now I want to get the first 8 digits from after
        sevenDigits = after[:7]
        lastTwoDigits = after.split('\'')[0][-2:]
        lastDeviation = str(deviation)
        print("lastDeviation", lastDeviation)
with open(f'test_data/result/result_data_{argNum}_dim_{dimension}_number_of_element_{number_of_element+1}.txt', 'w') as file:
            file.write("deviation:")
            file.write(lastDeviation)
