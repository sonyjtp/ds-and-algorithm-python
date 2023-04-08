# https://tinyurl.com/leetcode016
from collections import defaultdict


def can_construct_ransom_note():
    ransom_dict = defaultdict(int)
    for letter in ransom_note:
        ransom_dict[letter] += 1
    for letter in ransom_dict.keys():
        if magazine.count(letter) < ransom_dict[letter]:
            return False
    return True


ransom_note = "thorn"
magazine = "ornithorincus"
print(can_construct_ransom_note())
