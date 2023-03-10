import random

## wrong ##
# Given an integer array nums and an integer k,
# find the sum of the subarray with the largest sum whose length is k.
# def best_sub_array():
#     if len(nums) == k:
#         return sum(nums) / k
#     curr = sum(nums[:k])
#     new_sum = curr
#     for i in range(k, len(nums)):
#         new_sum += nums[i] - nums[i - k]
#         if new_sum > curr:
#             curr = new_sum
#     return curr / k
#
#
# nums = [random.randint(1, 8) for x in range(10)]
# k = random.randint(1, len(nums))
# print(f'nums:{nums}')
# print(f'size:{k}')
# print(best_sub_array())
