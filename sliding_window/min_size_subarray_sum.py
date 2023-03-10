# https://leetcode.com/problems/minimum-size-subarray-sum/

import random


def min_subarray_len():
    if sum(nums) < target:
        return 0
    left = sum_of_nums = 0
    num_len = len(nums)
    result = num_len
    for right in range(num_len):
        sum_of_nums += nums[right]
        while sum_of_nums >= target:
            result = min(result, right - left + 1)
            sum_of_nums -= nums[left]
            left += 1
    return result


nums = [random.randint(1, 10) for x in range(10)]
target = random.randint(20, 40)
print(nums)
print(target)
print(min_subarray_len())
