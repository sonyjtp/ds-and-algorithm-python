import random


# https://leetcode.com/problems/two-sum/
def two_sum():
    found = []
    added = []
    for i in range(len(nums)):
        if target - nums[i] in nums and nums.index(target - nums[i]) not in added:
            found.append((i, nums.index(target - nums[i])))
            added.append(i)
    return found


arr = [random.randint(1, 20) for x in range(1, 20)]
arr.sort()
nums = list(set(arr))
target = random.randint(1, 20)
print(f'nums: {nums}\ttarget: {target}\n{two_sum()}')
