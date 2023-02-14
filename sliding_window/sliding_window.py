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


nums = [random.randint(1, 5) for x in range(5)]
sum_ = random.randint(10, 20)
print(f'nums: {nums}')
print(f'sum: {sum_}')
print(sliding_window())
