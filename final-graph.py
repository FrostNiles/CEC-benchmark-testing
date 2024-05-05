import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import sys

function_numbers = [i for i in range(1, 31) if i not in [2, 9, 27]]

dimension = sys.argv[1]
dimension = int(dimension)
matlab_deviations = []  # create an empty list to store deviations
deviations = []  # create an empty list to store deviations

# load deviations from files
for i in range(1, 31):
    if i in [2, 9, 27]:
        continue
    with open(f'test_data/result/graph/C/lowest_dev_{i}_dim_{dimension}.txt', 'r') as file:
        contents = file.read()
        if 'Deviation:' in contents:
            deviation = contents.split(':')[1].strip()  # extract the deviation value
            deviation = deviation.split('\n')[0]
            deviation = float(deviation)
            deviations.append(deviation)  # add the deviation to the list
        else:
            print(f"File lowest_dev_{i}_dim_{dimension}.txt does not contain a ':'")

# load deviations from files
for i in range(1, 31):
    if i in [2, 9, 27]:
        continue
    with open(f'test_data/result/graph/Matlab/lowest_dev_{i}_dim_{dimension}.txt', 'r') as file:
        contents = file.read()
        if 'Deviation:' in contents:
            deviation = contents.split(':')[1].strip()  # extract the deviation value
            deviation = deviation.split('\n')[0]
            deviation = float(deviation)
            matlab_deviations.append(deviation)  # add the deviation to the list
        else:
            print(f"File lowest_dev_{i}_dim_{dimension}.txt does not contain a ':'")

plt.figure(figsize=(15, 10))
function_numbers = [i-1 if i != 1 else i for i in function_numbers]

# Define the width of a bar
bar_width = 0.4

# Positions of the left bar-boundaries
bar_l = [i + 1 for i in range(len(function_numbers))]

# Positions of the x-axis ticks (center of the bars as bar labels)
tick_pos = [i + (bar_width / 2) for i in bar_l]

# Create the bar plot for the first set of data
plt.bar(bar_l, deviations, width=bar_width, color='blue', label='C')

# Create the bar plot for the second set of data
plt.bar([p + bar_width for p in bar_l], matlab_deviations, width=bar_width, color='red', label='Matlab')

# Set the x-axis tick labels to the tick_pos list and the x-axis labels to the function_numbers list
plt.xticks(tick_pos, function_numbers)

plt.title(f'Odchylky funkcí CEC 2017, D={dimension}')
plt.xlabel('Číslo funkce')
plt.ylabel('Odchylka')
plt.yscale('log') 

plt.legend()

plt.savefig(f'../2017-D{dimension}.png', dpi=600)

#plt.show()