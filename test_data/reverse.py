import re

# Open the file and read its contents
with open('shift_data_1.txt', 'r') as file:
    data = file.read()
    print(data)

#open the backup file and read its contents
with open('shift_data_1_backup.txt', 'r') as file:
    backup_data = file.read()
    print(backup_data)

# backup the latest data
with open('shift_data_1_backup_latest.txt', 'w') as file:
    file.write(data)

# copy the backup data to the original file
with open('shift_data_1.txt', 'w') as file:
    file.write(backup_data)

