# https://tinyurl.com/leetcode012 (without sets)

# import random
from collections import defaultdict


def intersection():
    counts = defaultdict(int)
    ans = []
    no_of_arrays = len(nums)
    for arr in nums:
        for num in arr:
            counts[num] += 1
            if counts[num] == no_of_arrays:
                ans.append(num)
    return sorted(ans)


# nums = [[random.randint(1, 5) for x in range(1, random.randint(4, 6))] for y in range(3)]
nums = [[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]
print(nums)
print(intersection())
