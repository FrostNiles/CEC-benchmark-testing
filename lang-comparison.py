import sys
import matplotlib.pyplot as plt
import pandas as pd
import openpyxl

dimension = sys.argv[1]
dimension = int(dimension)
skipped = {2, 9}
if dimension == 50 or dimension == 100:
    skipped.add(27)

def load_deviations(filename, deviations_list):
    with open(filename, 'r') as file:
        result = file.read()
    result = result.split('deviation:')
    deviation = float(result[1])
    deviations_list.append(deviation)
    return deviations_list

data = []
deviations = []
matlab_deviations = []
matlab_bigger_than_c = 0
c_bigger_than_matlab = 0
c_equal_to_matlab = 0
deviation_differences = []

for i in range(1, 31):
    if i in skipped:
        continue
    for j in [dimension]:
        for k in range(1, j+1):   
            filename = f'test_data/result/result_data_{i}_dim_{j}_number_of_element_{k}.txt'
            matlab = f'../test2017-mat/test_data/result/result_data_{i}_dim_{j}_number_of_element_{k}.txt'
            
            deviations = load_deviations(filename, deviations)
            matlab_deviations = load_deviations(matlab, matlab_deviations)
           
    for index, (deviation, matlab_deviation) in enumerate(zip(deviations, matlab_deviations)):
        if deviation != matlab_deviation:
            deviation_differences.append(abs(deviation - matlab_deviation))
            if deviation > matlab_deviation:
                c_bigger_than_matlab += 1
            else:
                matlab_bigger_than_c += 1
        else:
            c_equal_to_matlab += 1
       
    print(f"func={i}")
    print("\n")
    
    data.append([
    i if i == 1 else i-1, 
    ('+' + str(matlab_bigger_than_c) if matlab_bigger_than_c != 0 else '') + ('/=' + str(c_equal_to_matlab) if c_equal_to_matlab != 0 and matlab_bigger_than_c != 0 else '=' + str(c_equal_to_matlab) if c_equal_to_matlab != 0 else '') + ('/-' + str(c_bigger_than_matlab) if c_bigger_than_matlab != 0 else ''), 
])
            
    
    # Compare the three lists
    deviations = []
    matlab_deviations = []
    c_bigger_than_matlab = 0
    matlab_bigger_than_c = 0
    c_equal_to_matlab = 0



# Create a new figure with a specific size (fullscreen)
fig, ax = plt.subplots(figsize=(14, 10))

# Hide axes
ax.axis('off')

# Create a table and add it to the axes
table = ax.table(cellText=data, colLabels=['Číslo funkce (F*)', 'C/MATLAB'], loc='center', cellLoc = 'center')

# Scale the cells' size
table.scale(1, 2)

# Center the data in the cells
table.auto_set_font_size(False)
table.set_fontsize(10)
for key, cell in table.get_celld().items():
    cell.set_linewidth(1)  # Add border to cells
    cell.set_fontsize(14)
    cell.set_text_props(ha='center')

# Make the first row and column bold
for i in range(len(data[0])):
    table[(0, i)].set_fontsize(14)
    table[(0, i)].set_text_props(weight='bold', color='k')
for i in range(len(data)+1):
    table[(i, 0)].set_fontsize(14)
    table[(i, 0)].set_text_props(weight='bold', color='k')

# Save the figure in fullscreen
#plt.savefig(f'table-2022-{dimension}.png', dpi=600, bbox_inches='tight', bbox_extra_artists=[table])

# Show the plot
plt.show()

# Create a DataFrame from your data
df = pd.DataFrame(data, columns=['Číslo funkce (F*)', 'C/MATLAB'])

# Set the first column as index
df.set_index('Číslo funkce (F*)', inplace=True)

# Export the DataFrame to a CSV file
df.to_csv(f'table-2017-{dimension}.csv')
df.to_excel(f'table-2017-{dimension}.xlsx')