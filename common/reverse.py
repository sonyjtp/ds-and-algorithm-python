import math


def reverse():
    for i in range(math.floor(len(arr) / 2)):
        j = arr[i]
        arr[i] = arr[len(arr) - 1 - i]
        arr[len(arr) - 1 - i] = j


arr = ["h", "e", "l", "l", "o"]
reverse()
print(arr)
