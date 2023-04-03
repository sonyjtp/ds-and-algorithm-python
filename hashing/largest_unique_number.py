from collections import defaultdict
import random
# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4662/

def largest_unique_number():
    num_dict = defaultdict(int)
    removed = set()
    for num in nums:
        num_dict[num] += 1
        if num_dict[num] > 1:
            removed.add(num)
    return max(num_dict.keys() - removed) if len(removed) != len(num_dict.keys()) else -1


nums = [random.randint(1, 12) for x in range(9)]
print(nums)
print(largest_unique_number())
