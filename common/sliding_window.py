# Given an array of positive integers nums and an integer k, find
# the length of the longest subarray whose sum is less than or equal to k
import math
# add elements to the right; if the constraint is broken, remove elements from the left

import random


def sliding_window():
    curr = left = result = 0
    for right in range(len(nums)):
        curr += nums[right]
        while curr > sum_:
            curr -= nums[left]
            left += 1
        result = max(result, right - left + 1)
    return result


# find how many sub_arrays whose product is less than a target
def sliding_window_2():
    if pdt <= 1:
        return 0
    product = 1
    result = 0
    left = 0
    for right in range(len(nums)):
        product *= nums[right]
        while product >= pdt:
            product /= nums[left]
            left += 1
        result += right - left + 1
    return result


nums = [random.randint(1, 5) for x in range(5)]
sum_ = random.randint(10, 20)
pdt = random.randint(10, 20)
print(f'nums: {nums}')
print(f'sum: {sum_}')
print(sliding_window())
print(f'product: {pdt}')
print(sliding_window_2())
