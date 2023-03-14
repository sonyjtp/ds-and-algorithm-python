# https://tinyurl.com/leetcode009

import random


def missing_number():
    nums.sort()
    for i in range(0, len(nums)):
        if i != nums[i]:
            return i
    return len(nums)


nums = [x for x in range(0, 10001)]
nums.remove(random.randint(1, 1000))
random.shuffle(nums)
print(nums)
print(missing_number())
