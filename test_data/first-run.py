import re

# Open the file and read its contents
with open('shift_data_1_backup.txt', 'r') as file:
    data = file.read()

# open the latest backup file and read its contents
with open('shift_data_1_backup_latest.txt', 'r') as file:
    backup_latest_data = file.read()

# Split the data into individual numbers - the one number is written like this (for example) in the file -5.527639849e+01

data_numbers = re.findall(r'[-+]?\d*\.\d+|\d+', data)
backup_numbers = re.findall(r'[-+]?\d*\.\d+|\d+', backup_latest_data)



# ok lets convert those number - there are always two numbers after each other in the list the first is the float number and the second is the power of 10
# I want to convert them to the float number
data_numbers = [float(data_numbers[i]) * 10**int(data_numbers[i+1]) for i in range(0, len(data_numbers), 2)]



backup_numbers = [float(backup_numbers[i]) * 10**int(backup_numbers[i+1]) for i in range(0, len(backup_numbers), 2)]



# now I want to bisecting the interval between the two numbers on the same position in each file
# I want to get the number in the middle between the two numbers with bisecting the interval

middle_numbers = [(data_numbers[i] + backup_numbers[i]) / 2 for i in range(len(data_numbers))]


# now I want to write the middle numbers to the original file just the number and with a space behind the number
with open('shift_data_1.txt', 'w') as file:
    for number in middle_numbers:
        file.write(f"{number} ")


