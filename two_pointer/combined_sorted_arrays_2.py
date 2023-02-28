import random


def combine_sorted_arrays():
    result = []
    i = j = 0
    while i < len(arr_1) and j < len(arr_2):
        if arr_1[i] < arr_2[j]:
            result.append(arr_1[i])
            i += 1
        else:
            result.append(arr_2[j])
            j += 1

    while i < len(arr_1):
        result.append(arr_1[i])
        i += 1

    while j < len(arr_2):
        result.append(arr_2[j])
        j += 1

    return result


arr_1 = [random.randint(4, 15) for x in range(7)]
arr_1.sort()
arr_2 = [random.randint(3, 18) for x in range(8)]
arr_2.sort()
print(f'1st: {arr_1}\n2nd: {arr_2}')
print(f'Combined: {combine_sorted_arrays()}')
