# https://tinyurl.com/leetcode003

# Given an array of integers nums, you start with an initial positive value startValue.
# In each iteration, you calculate the step by step sum of startValue plus elements in nums( from left to right).
# Return the minimum positive value of startValue such that the step by step sum is never less than 1.
#
# Example
# Input: nums = [-3, 2, -3, 4, 2]
# Output: 5
# Explanation: If you choose startValue = 4, in the third iteration your step by step sum is less than 1.
#
# Step by step sum
# startValue = 4 | startValue = 5 | nums
# (4 - 3) = 1 | (5 - 3) = 2 | -3
# (1 + 2) = 3 | (2 + 2) = 4 | 2
# (3 - 3) = 0 | (4 - 3) = 1 | -3
# (0 + 4) = 4 | (1 + 4) = 5 | 4
# (4 + 2) = 6 | (5 + 2) = 7 | 2

import random


def min_start_value():
    result = 1 if nums[0] > 0 else 1 - nums[0]
    prefix_sum = nums[0]
    arr_len = len(nums)
    for i in range(1, arr_len):
        prefix_sum = prefix_sum + nums[i]
        if prefix_sum < 1:
            result = max(result, 1 - prefix_sum)
    return result


nums = [random.randint(-5, 5) for x in range(8)]
print(nums)
print(min_start_value())
