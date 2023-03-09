# https://tinyurl.com/leetcode001
import random


def prefix_sum():
    valid = prefix = 0
    sum_of_numbers = sum(nums)
    print(sum_of_numbers)
    for i in range(arr_len - 1):
        prefix += nums[i]
        if prefix >= sum_of_numbers - prefix:
            valid += 1
    return valid


arr_len = int(input("length of array: "))
nums = [random.randint(0, 10) for x in range(arr_len)]
print(nums)
print(prefix_sum())

