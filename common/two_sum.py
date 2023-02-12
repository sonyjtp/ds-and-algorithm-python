import random


def two_sum_1():
    found = []
    added = []
    for i in range(0, len(nums)):
        if target - nums[i] in nums and nums.index(target - nums[i]) not in added:
            found.append((i, nums.index(target - nums[i])))
            added.append(i)
    return found


def two_sum_2():
    found = []
    i = 0
    j = len(nums) - 1
    prev_i = i
    prev_j = j
    while i < j:
        if nums[i] + nums[j] == target:
            found.append((i, j))
            i = prev_i + 1
            prev_i = i
            j = prev_j - 1
            prev_j = j
        elif nums[i] + nums[j] > target:
            j -= 1
        else:
            i += 1
    return found


arr = [random.randint(1, 20) for x in range(1, 20)]
arr.sort()
nums = list(set(arr))
target = random.randint(1, 20)
print(f'nums: {nums}')
print(f'target: {target}')
# print(two_sum_1())
print(two_sum_2())
