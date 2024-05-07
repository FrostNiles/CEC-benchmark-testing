import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np


function_numbers = [i for i in range(1, 31) if i not in [2, 9]]

dimension = 10
number_of_element = 1
deviations = []  # create an empty list to store deviations

# load deviations from files
for i in range(1, 31):
    if i in [2, 9]:
        continue
    with open(f'test_data/result/result_data_{i}_dim_{dimension}_number_of_element_{number_of_element}.txt', 'r') as file:
        contents = file.read()
        if ':' in contents:
            deviation = contents.split(':')[1].strip()  # extract the deviation value
            deviation = float(deviation)
            deviations.append(deviation)  # add the deviation to the list
        else:
            print(f"File result_data_{i}_dim_{dimension}_number_of_element_{number_of_element}.txt does not contain a ':'")
""" print(deviations)
print(function_numbers) """
# print the numbers without space between them
# I need to extract the deviation value from the string
# Change the format of the y-axis labels


plt.figure(figsize=(12, 12))
function_numbers = [i-1 if i != 1 else i for i in function_numbers]

plt.bar(np.arange(len(function_numbers)), deviations, color='blue')

formatter = ticker.FuncFormatter(lambda x, pos: '{:.15f}'.format(x))
plt.gca().yaxis.set_major_formatter(formatter)

plt.title('Odchylky funkcí')
plt.xlabel('Číslo funkce')
plt.ylabel('Odchylka')
#plt.yscale('log') 
plt.xticks(np.arange(len(function_numbers)), function_numbers)

plt.show()