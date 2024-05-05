import runpy
import re
import sys

arg1 = sys.argv[1]
arg2 = sys.argv[2]
arg3 = sys.argv[3]

# Run the first Python script
argNum = arg1
dimension = arg2

sys.argv = ['run-tests.py', arg1, arg2, arg3]
#import the original data

runpy.run_path('./import-original.py')
runpy.run_path('./run-main.py')

# Open the dimension file and func_num file and read its contents

with open(f'test_data/current_result_{argNum}.txt', 'r') as file:
    result = file.read()

# Find the number in the string
result = re.findall(r'\d+\.\d+', result)

# Keep the number as a string to preserve trailing zeroes
number_string = result[0]

# Convert to float when you need to do a numerical operation

result = str(result)
result = result.split('.')
#before the floating point
before = result[0]
#after the floating point
after = result[1]

# Now I want to get the first 8 digits from after
eightDigits = after[:8]
lastTwoDigits = after[-2:]
counter_first = 0
while int(eightDigits) == 0:
    runpy.run_path('./delete-floating-point.py')
    runpy.run_path('./run-main.py')
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

    eightDigits = after[:8]
    lastTwoDigits = after[-2:]
    counter_first += 1
    if counter_first == 40:
        sys.exit()

with open(f'test_data/shift_data_{argNum}.txt', 'r') as file:
    data = file.read()

with open(f'test_data/shift_data_{argNum}_backup.txt', 'r') as file:
    backup = file.read()

# lets write both data and backup to the file separete them with enter
with open(f'test_data/shift_data_{argNum}_final.txt', 'w') as file:
    file.write(backup)
    file.write("\n")
    file.write(data)


number_of_element = int(arg3) - 1
data_number = re.findall(r'\d*\.?\d*e[+-]\d+', data)[number_of_element]
backup_number = re.findall(r'\d*\.?\d*e[+-]\d+', backup)[number_of_element]



#write only one of the data to the file
with open(f'test_data/result/result_data_{argNum}_dim_{dimension}_number_of_element_{number_of_element+1}.txt', 'w') as file:
    file.write(f"Dimension: {dimension}")
    file.write("\n")
    file.write(data_number)
    file.write("\n")
    file.write(backup_number)
    file.write("\n")
with open(f'test_data/shift_data_{argNum}.txt', 'w') as file:
    file.write(data)

with open(f'test_data/shift_data_{argNum}_backup.txt', 'w') as file:
    file.write(backup)

#stop here for now
#sys.exit()



runpy.run_path('./first-run.py')

runpy.run_path('./convert-e-to-float.py')

runpy.run_path('./run-main.py')


#open the result file
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
eightDigits = after[:8]
lastTwoDigits = after[-2:]


counter = 0

while int(eightDigits) > 0 or int(lastTwoDigits) < 96:
    
    runpy.run_path('./help-bisecting.py')
    
    runpy.run_path('./half.py')
    
    runpy.run_path('./run-main.py')
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

    eightDigits = after[:8]
    lastTwoDigits = after[-2:]
    counter += 1
    if counter == 50:
        runpy.run_path('./anomaly-deviation.py')


#open the shift_data_1.txt and read the data
with open(f'test_data/shift_data_{argNum}.txt', 'r') as file:
    data = file.read()
#write these results to the file shift_data_1final_bisection.txt
with open(f'test_data/shift_data_{argNum}_final_bisection.txt', 'w') as file:
    file.write(data)


runpy.run_path('./deviation.py')
runpy.run_path('./inspection.py')
runpy.run_path('./run-main.py')

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
eightDigits = after[:8]

lastTwoDigits = after[-2:]
tenDigits = after[:10]

# Add more lines as needed to run more scripts

with open(f'test_data/shift_data_{argNum}_deviation_final.txt', 'r') as file:
                deviation = file.read()

with open(f'test_data/result/result_data_{argNum}_dim_{dimension}_number_of_element_{number_of_element+1}.txt', 'w') as file:
    file.write("deviation:")
    file.write(deviation)
    