# find how many sub_arrays whose product is less than a target

import random


def sliding_window_2():
    if pdt <= 1:
        return 0
    product = 1
    result = 0
    left = 0
    for right in range(len(nums)):
        product *= nums[right]
        while product >= pdt:
            product /= nums[left]
            left += 1
        result += right - left + 1
    return result


nums = [random.randint(1, 5) for x in range(5)]
pdt = random.randint(10, 20)
print(f'nums: {nums}')
print(f'product: {pdt}')
print(sliding_window_2())
