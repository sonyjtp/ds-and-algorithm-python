# https://leetcode.com/problems/two-sum/
import random


def two_sum():
    for i in range(len(nums)):
        if target - nums[i] in nums and i != nums.index(target - nums[i]):
            return [i, nums.index(target - nums[i])]


arr = [random.randint(1, 20) for x in range(1, 20)]
nums = list(set(arr))
target = random.randint(1, 20)
print(f'nums: {nums}\ttarget: {target}\n{two_sum()}')

