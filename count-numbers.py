import sys
argNum = sys.argv[1]
file_path = f"test_data/shift_data_{argNum}.txt"
# these are the first two numbers "   9.5857011347942525e+00   7.3284069743605357e+01  " also with those spaces in file
with open(file_path, 'r') as file:
    contents = file.read()

# find how many e+ or e- in the file
count = contents.count("e+") + contents.count("e-")
print(count)
