# https://tinyurl.com/max-cons-ones

import random


def max_consecutive_ones():
    if k > nums.count(0):
        return len(nums)
    left = right = longest = count_of_zeros = 0
    while right < len(nums):
        if nums[right] == 0:
            count_of_zeros += 1
        while count_of_zeros > k:
            if nums[left] == 0:
                count_of_zeros -= 1
            left += 1
        longest = max(right - left + 1, longest)
        right += 1
    return longest


nums = [random.randint(0, 1) for x in range(12)]
k = random.randint(2, 5)
print(f'array: {nums}\tk: {k}')
print(max_consecutive_ones())
