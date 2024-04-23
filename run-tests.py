import runpy
import re
import sys

# Run the first Python script
argNum = sys.argv[1]
dimension = sys.argv[2]

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
print("lastTwoDigits:",lastTwoDigits)
print("eightDigits:",eightDigits)

while int(eightDigits) == 0:
    print("The result is bigger than 99")
    runpy.run_path('./delete-floating-point.py')
    runpy.run_path('./run-main.py')
    with open(f'test_data/current_result_{argNum}.txt', 'r') as file:
        result = file.read()

    result = re.findall(r'\d+\.\d+', result)
    print("result:",result)
    result = float(result[0])
    print("result float result[0]:",result)

    result = str(result)
    result = result.split('.')
    #before the floating point
    before = result[0]
    #after the floating point
    after = result[1]

    eightDigits = after[:8]
    lastTwoDigits = after[-2:]
    print("eightDigits:",eightDigits)
    print("lastTwoDigits:",lastTwoDigits)

with open(f'test_data/shift_data_{argNum}.txt', 'r') as file:
    data = file.read()

with open(f'test_data/shift_data_{argNum}_backup.txt', 'r') as file:
    backup = file.read()

# lets write both data and backup to the file separete them with enter
with open(f'test_data/shift_data_{argNum}_final.txt', 'w') as file:
    file.write(backup)
    file.write("\n")
    file.write(data)


number_of_element = int(sys.argv[3]) - 1
data_number = re.findall(r'\d+\.\d+e[+-]\d+', data)[number_of_element]
backup_number = re.findall(r'\d+\.\d+e[+-]\d+', backup)[number_of_element]

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
print("eightDigits:",eightDigits)
print("lastTwoDigits:",lastTwoDigits)


while int(eightDigits) > 0 or int(lastTwoDigits) < 96:
    
    print("in while loop")
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
print("eightDigits:",eightDigits)
lastTwoDigits = after[-2:]
tenDigits = after[:10]

if int(eightDigits) > 0:

    while int(eightDigits) != 0:
        print("The result is bigger than expected after run")
        #load median deviation
        with open(f'test_data/shift_data_{argNum}_deviation_final.txt', 'r') as file:
            median_deviation = file.read()
        #change the median deviation
        #check the first two digits after the floating point
        median_deviation = str(median_deviation)
        median_deviation = median_deviation.split('.')
        #before the floating point
        before = median_deviation[0]
        

        if len(before) > 1:
            if before[1] == 'e':
                print("before[1] is e")
                backup = before.split('e')
                if before[0] == '0':
                    print("before[0] is 0")
                    before = '9'
                    backup[1] = int(backup[1]) - 1
                    backup[1] = str(backup[1])
                    median_deviation = before + "." + "" + "e" + backup[1]
                else:
                    print("before[0] is not 0")
                    before = before.split('e')
                    before[0] = int(before[0]) - 1
                    before = str(before[0]) 
                    median_deviation = before + "." + "99" + "e" + backup[1]
            else:
                print("before[1] is not e")
                #after the floating point
                after = median_deviation[1]
                # Now I want to get the first 2 digits from after
                twoDigits = after[:2]
                if twoDigits[1] == 'e':
                    print("twoDigits[1] is e")
                    if twoDigits[0] == '1':
                        print("twoDigits[0] is 1")
                        twoDigits = '0' + '9'
                        twoDigits = int(twoDigits) -1
                    else:
                        print("twoDigits[0] is not 1")
                        twoDigits = twoDigits[0] + '0'
                        twoDigits = int(twoDigits) - 1
                else:
                    print("twoDigits[1] is not e")
                    twoDigits = int(twoDigits) - 1
                    
                #and also I want to get e-01 or whatever is there after "e" and after is like this: 5056482283171135e-08
                exponent = after.split('e')[1]
                twoDigits = f"{twoDigits:02d}"
                #substract 1 from the first two digits
                
                #concatenate the before and the two digits
                median_deviation = before + "." + twoDigits + "e" + exponent
                
        else:
            print("before is 1 digit")
            print("before:",before)
            if (int(eightDigits) > 3):
                print("eightDigits is bigger than 3")
                before = int(before) - 1
                before = str(before)
            #after the floating point
            after = median_deviation[1]
            # Now I want to get the first 2 digits from after
            twoDigits = after[:2]
            if twoDigits[1] == 'e':
                print("twoDigits[1] is e")
                if twoDigits[0] == '1':
                    print("twoDigits[0] is 1")
                    twoDigits = '0' + '9'
                    twoDigits = int(twoDigits) -1
                else:
                    print("twoDigits[0] is not 1")
                    twoDigits = twoDigits[0] + '0'
                    twoDigits = int(twoDigits) - 1
            elif twoDigits == '00':
                print("twoDigits is 00")
                twoDigits = '99'
                twoDigits = int(twoDigits)
                before = int(before) - 1
                before = str(before)
            else:
                print("twoDigits[1] is not e")
                twoDigits = int(twoDigits) - 1
                
            #and also I want to get e-01 or whatever is there after "e" and after is like this: 5056482283171135e-08
            exponent = after.split('e')[1]
            twoDigits = f"{twoDigits:02d}"
            #substract 1 from the first two digits
            
            #concatenate the before and the two digits
            median_deviation = before + "." + twoDigits + "e" + exponent
                
        print("median deviation:",median_deviation)
        #write the new median deviation to the file
        with open(f'test_data/shift_data_{argNum}_deviation_final.txt', 'w') as file:
            file.write(median_deviation)
        
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
        eightDigits = after[:8]
        lastTwoDigits = after[-2:]
        tenDigits = after[:10]
        print("eightDigits:",eightDigits)
    

    

else:
    if int(lastTwoDigits) < 96:
        while int(lastTwoDigits) < 96:
            print("The result is lower than expected after run")
            #load median deviation
            with open(f'test_data/shift_data_{argNum}_deviation_final.txt', 'r') as file:
                median_deviation = file.read()
            #change the median deviation
            #check the first two digits after the floating point
            median_deviation = str(median_deviation)
            median_deviation = median_deviation.split('.')
            #before the floating point
            before = median_deviation[0]

            if len(before) > 1:
                print("before is bigger than 1")
                if before[1] == 'e':
                    print("before[1] is e")
                    backup = before.split('e')
                    before = before.split('e')
                    before[0] = int(before[0])
                    before = str(before[0]) 
                    median_deviation = before + "." + "01" + "e" + backup[1]
        
            else:
                print("before is 1 digit")
                if (int(tenDigits) < 40):
                    print("tenDigits is lower than 40")
                    digitCount = len(str(int(tenDigits)))
                    
                    if digitCount == 2:  
                        print("tenDigits is 2 digits")  
                        before = int(before) + 1
                        before = str(before)
                #after the floating point
                after = median_deviation[1]
                # Now I want to get the first 2 digits from after
                twoDigits = after[:2]
                #and also I want to get e-01 or whatever is there after "e" and after is like this: 5056482283171135e-08
                
                exponent = after.split('e')[1]
                
            
                if twoDigits == '99':
                    print("twoDigits is 99")

                    if (before == '9'):
                        print("before is 9")
                        exponent = int(exponent) + 1
                        exponent = str(exponent)
                        before = '1'
                    else:
                        print("before is not 9")
                        before = int(before) + 1
                        before = str(before)
                    twoDigits = '00'
                    median_deviation = before + "." + twoDigits + "e" + exponent
                else:
                    print("twoDigits is not 99")
                    if twoDigits[1] == 'e':
                        print("twoDigits[1] is e")
                        twoDigits = twoDigits[0] + '0'
                        #concatenate the before and the two digits
                        median_deviation = before + "." + twoDigits + "e" + exponent
                    if twoDigits[0] == '0':
                        print("twoDigits[0] is 0")
                        if twoDigits[1] == '9':
                            print("twoDigits[1] is 9")
                            twoDigits = "10"
                            #concatenate the before and the two digits
                            median_deviation = before + "." + twoDigits + "e" + exponent
                        else:
                            print("twoDigits[1] is not 9")
                            twoDigits = int(twoDigits) + 1
                            #convert the two digits to string
                            twoDigits = str(twoDigits)
                            twoDigits = '0' + twoDigits
                            #concatenate the before and the two digits
                            median_deviation = before + "." + twoDigits + "e" + exponent
                    else:
                        print("twoDigits[0] is not 0")
                        twoDigits = int(twoDigits) + 1
                        #convert the two digits to string
                        twoDigits = str(twoDigits)
                        #concatenate the before and the two digits
                        median_deviation = before + "." + twoDigits + "e" + exponent
            print(median_deviation)
            #write the new median deviation to the file
            with open(f'test_data/shift_data_{argNum}_deviation_final.txt', 'w') as file:
                file.write(median_deviation)
            
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
            eightDigits = after[:8]
            lastTwoDigits = after[-2:]
            tenDigits = after[:10]
# Add more lines as needed to run more scripts

with open(f'test_data/shift_data_{argNum}_deviation_final.txt', 'r') as file:
                deviation = file.read()

with open(f'test_data/result/result_data_{argNum}_dim_{dimension}_number_of_element_{number_of_element+1}.txt', 'w') as file:
    file.write("deviation:")
    file.write(deviation)
    