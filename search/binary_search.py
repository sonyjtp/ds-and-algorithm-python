from bisect import bisect_left
import random
import time


def binary_search(lst, target):
    lo = 0
    hi = len(lst)
    ind = bisect_left(lst, target, lo, hi)
    if 0 <= ind < hi and lst[ind] == target:
        return ind
    return -1


print("Search each number in a list")
count = input("List size: ")
numbers = [random.randint(1, int(count)) for x in range(1, 100000)]
start = time.time()
for i in numbers:
    binary_search(numbers, i)
end = time.time()
print(f"Time taken to search {count} numbers: " + "{:.5f}".format(round((end - start) / 1000.000000), 3) + " seconds")
