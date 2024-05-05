import sys

dimension = sys.argv[1]
dimension = int(dimension)


def load_deviations(filename, deviations):
    with open(filename, 'r') as file:
        result = file.read()
    result = result.split('deviation:')
    deviation = float(result[1])
    deviations.append(deviation)
    return deviations

def get_highest_deviation(deviations):
    highest_deviation = max(deviations)
    with open(f'test_data/result/highest_dev_{i}_dim_{j}.txt', 'w') as file:
        file.write(f"Deviation: {highest_deviation}")
        file.write("\n")
        file.write(f"Position: {deviations.index(highest_deviation)+1}")
    return highest_deviation

def get_lowest_deviation(deviations):
    lowest_deviation = min(deviations)
    with open(f'test_data/result/lowest_dev_{i}_dim_{j}.txt', 'w') as file:
        file.write(f"Deviation: {lowest_deviation}")
        file.write("\n")
        file.write(f"Position: {deviations.index(lowest_deviation)+1}")
    return lowest_deviation

deviations = []
skipped = {2, 9, 27}
for i in range(1, 31):
    if i in skipped:
        continue
    for j in [dimension]:
        for k in range(1, j+1):   
            filename = f'test_data/result/result_data_{i}_dim_{j}_number_of_element_{k}.txt'
            deviations = load_deviations(filename, deviations)
    deviations = load_deviations(filename, deviations)
    lowest_deviation = get_lowest_deviation(deviations)
    deviations = []
  


""" deviations = load_deviations(filename, deviations)
lowest_deviation = get_lowest_deviation(deviations)
print(f"The lowest deviation for {filename} is: {lowest_deviation}") """