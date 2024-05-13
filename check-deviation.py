import sys
import runpy
import re
import math

skipped = [2, 9]
""" argNum = sys.argv[1]
dimension = sys.argv[2]
number_of_element = int(sys.argv[3]) - 1 """

for i in range(15, 31):
    if i in skipped:
        continue
    for j in [10, 30, 50, 100]:
        if j == 50 or j == 100 and i == 27:
            continue
        for k in range(1, j+1):
            if i == 10 and k == 44:
                continue
            argNum = i
            dimension = j
            number_of_element = k

            # Read the original numbers
            with open(f'input_data/shift_data_{argNum}.txt', 'r') as file:
                original_data = file.read()

            # read the deviation


            with open(f'test_data/result/result_data_{argNum}_dim_{dimension}_number_of_element_{number_of_element}.txt', 'r') as file:
                data = file.read()

            # Extract the numbers from the lines
            data = data.split('deviation:')
            deviation = float(data[1])
            print("deviation", deviation)

            # now +/- from the original data on the number_of_element position the deviation
            original_numbers = [float(i) for i in original_data.split()]

            if deviation == math.inf:
                original_numbers[number_of_element-1] = 0.0    
            else:
                original_numbers[number_of_element-1] = original_numbers[number_of_element-1] - deviation

            with open(f'test_data/shift_data_{argNum}.txt', 'w') as file:
                for number in original_numbers:
                    file.write(f"{number} ")

            # Prepare the arguments
            args = ['./run-main.py', str(argNum), str(dimension), str(number_of_element)]

            # Set the arguments
            sys.argv = args
            runpy.run_path('./run-main.py' )

            # open the result file
            with open(f'test_data/current_result_{argNum}.txt', 'r') as file:
                result = file.read()

            result = re.findall(r'\d+\.\d+', result)
            result = float(result[0])
            result = str(result)
            result = result.split('.')
            #before the floating point
            before = result[0]
            #after the floating point
            after = result[1]


            # Now I want to get the first 8 digits from after
            sevenDigits = after[:7]

            lastTwoDigits = after[-2:]

            if int(sevenDigits) != 0:
                print(i, j, k)
                print("The deviation is not correct")
                sys.exit(1)
