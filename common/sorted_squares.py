import random

from sort.merge_sort import merge_sort


def sorted_squares():
    squares = [pow(x, 2) for x in nums]
    merge_sort(squares)
    return squares


nums = [random.randint(-5, 10) for x in range(1, 20)]
print(f"nums: {nums}")
print(f"sorted squares: {sorted_squares()}")
