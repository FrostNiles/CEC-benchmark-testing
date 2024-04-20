import re
import sys

argNum = sys.argv[1]
numberOfDelete = sys.argv[3]
# Open the file and read its contents
with open(f'test_data/shift_data_{argNum}.txt', 'r') as file:
    data = file.read()

#write original content to backup file
with open(f'test_data/shift_data_{argNum}_backup.txt', 'w') as file:
    file.write(data)

# Use a regular expression to replace numbers before "e" with an empty string
# just delete one number before "e"
# in the end I want to get the whole number just without the digit before "e"
# but I want to delete only from one number and its position I will tell in the argument
# so I will delete the number before "e" from the number which is in the position 1

#modified_data = re.sub(r'(\d)(e)', r'\2', data)
modified_data = re.sub(r'(\d)(e)', r'\2', data, int(numberOfDelete)-1)


# Write the modified contents to the original file
with open(f'test_data/shift_data_{argNum}.txt', 'w') as file:
    file.write(modified_data)