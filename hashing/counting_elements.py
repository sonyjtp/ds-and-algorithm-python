# https://tinyurl.com/leetcode010

import random


def counting_elements():
    nums.sort()
    print(f'sorted numbers: {nums}')
    count = i = 0
    same_nums = 1
    while i < len(nums) - 1:
        if nums[i + 1] == nums[i]:
            while i < len(nums) - 1 and nums[i + 1] == nums[i]:
                same_nums += 1
                i += 1
        if i < len(nums) - 1 and nums[i + 1] == nums[i] + 1:
            count += same_nums
        same_nums = 1
        i += 1
    return count


nums = [random.randint(1, 15) for x in range(1, 20)]
random.shuffle(nums)
print(nums)
print(counting_elements())
