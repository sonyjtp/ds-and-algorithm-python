# You are given a string s and an integer k.
# Find the length of the longest substring that contains at most k distinct characters.

import random
from collections import defaultdict


def longest_substring():
    char_dict = defaultdict(int)
    left = longest = 0
    for right in range(len(arr)):
        char_dict[arr[right]] += 1
        while len(char_dict) > k:
            char_dict[arr[left]] -= 1
            if char_dict[arr[left]] == 0:
                del char_dict[arr[left]]
            left += 1
        longest = max(longest, right - left + 1)
    return longest


arr = [chr(random.randint(97, 106)) for x in range(10)]
k = random.randint(3, 5)
print(arr)
print(k)
print(longest_substring())
