# https://tinyurl.com/leetcode002
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).


import random


def prefix_sum():
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[i - 1])
    return prefix


nums = [random.randint(1, 10) for x in range(5)]
print(f'nums: {nums}\n')
print(prefix_sum())
