import sys

skipped = {2, 9, 27}

for i in range(1, 31):
    if i in skipped:
        continue
    # check the results if there is a deviation
    for j in [10, 30, 50, 100]:
        for k in range(1, j+1):   
            """ if i == 14 and j == 100 and k == 51:
                continue    """ 
            with open(f'test_data/result/result_data_{i}_dim_{j}_number_of_element_{k}.txt', 'r') as file:
                result = file.read()
            # if not "deviation:" in result:
            # sys.exit()
            result = result.split('deviation:')
            print(i, j, k)
            print(result[1])
            