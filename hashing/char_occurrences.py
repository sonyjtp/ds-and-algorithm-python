# https://tinyurl.com/leetcode013
from collections import defaultdict


def are_all_occurrences_equal(string):
    char_dict = defaultdict(int)
    counts = 0
    for char in string:
        char_dict[char] += 1
    counts = char_dict.values()
    return len(set(counts)) == 1


print(are_all_occurrences_equal('abacbc'))
