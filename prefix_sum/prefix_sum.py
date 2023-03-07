# Given an integer array nums, an array queries where queries[i] = [x, y] and an integer limit,
# return a boolean array that represents the answer to each query.
# A query is true if the sum of the subarray from x to y is less than limit, or false otherwise.
# For example, given nums = [1, 6, 3, 2, 7, 2] and queries = [[0, 3], [2, 5], [2, 4]] and limit = 13,
# the answer is [true, false, true]. For each query, the subarray sums are [12, 14, 12].

import random


def prefix_sum():
    prefix = [nums[0]]
    result = []
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[i - 1])
    for query in queries:
        sum_of_subarray = prefix[query[1]] - prefix[query[0]] + nums[query[0]]
        result.append(sum_of_subarray < limit)
    return result


nums = [random.randint(1, 10) for x in range(15)]
queries = [[random.randint(0, 5), random.randint(5, 9)] for x in range(6)]
limit = random.randint(20, 30)
print(f'nums: {nums}\nqueries: {queries}\nlimit: {limit}')
print(prefix_sum())
