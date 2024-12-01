list_1 = []
list_2 = []

with open("./input.txt", 'r') as file:
    for line in file:
        line = line.split()
        list_1.append(int(line[0]))
        list_2.append(int(line[1]))


def calculate_sum_of_smallest_distances(arr_1, arr_2):
    arr_1.sort()
    arr_2.sort()
    total = 0

    for i, el in enumerate(arr_1):
        distance = abs(el - arr_2[i])
        total += distance

    return total


distances = calculate_sum_of_smallest_distances(list_1, list_2)
print("Solution 1: " + str(distances))


def similarity_score(arr_1, arr_2):
    similarity = 0
    for _, el in enumerate(arr_1):
        count = arr_2.count(el)
        similarity += el * count
    return similarity


similarity_score = similarity_score(list_1, list_2)
print("Similarity Score: " + str(similarity_score))
