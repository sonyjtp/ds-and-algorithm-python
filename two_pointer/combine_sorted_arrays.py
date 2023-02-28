import random


def combine_sorted_arrays():
    if arr_2 is None or len(arr_2) == 0:
        return arr_1
    if arr_1 is None or len(arr_1) == 0:
        return arr_2
    result = []
    j = 0
    for i in range(len(arr_1)):
        while j < len(arr_2) and arr_2[j] < arr_1[i]:
            result.append(arr_2[j])
            j += 1
        if j == len(arr_2):
            result += arr_1[i:]
            break
        result.append(arr_1[i])
    if len(result) < len(arr_1) + len(arr_2):
        result.append(arr_2[len(arr_2) - j:])
    return result


arr_1 = [random.randint(5, 22) for x in range(7)]
arr_1.sort()
arr_2 = [random.randint(3, 20) for x in range(8)]
arr_2.sort()
print(f'1st: {arr_1}\n2nd: {arr_2}')
print(f'Combined: {combine_sorted_arrays()}')
