import re

# Open the file and read its contents
with open('shift_data_1.txt', 'r') as file:
    data = file.read()
    print(data)

#write original content to backup file
with open('shift_data_1_backup.txt', 'w') as file:
    file.write(data)

# Use a regular expression to replace numbers before "e" with an empty string
# just delete one number before "e"
# in the end I want to get the whole number just without the digit before "e"
modified_data = re.sub(r'(\d)(e)', r'\2', data)
print("Modified data: ", modified_data)


# Write the modified contents to the original file
with open('shift_data_1.txt', 'w') as file:
    file.write(modified_data)