# https://tinyurl.com/leetcode005
# Given a string s and an integer k,
# return the maximum number of vowel letters in any substring of s with length k.
import random


def max_vowels():
    vowels = 'aeiou'
    longest = curr = len([x for x in arr[:k] if x in vowels])
    for right in range(k, len(arr)):
        if arr[right] in vowels:
            curr += 1
        if arr[right - k] in vowels:
            curr -= 1
        longest = max(longest, curr)
    return longest


#
arr = [chr(random.randint(97, 122)) for x in range(5)] + [
    ['a', 'e', 'i', 'o', 'u'][random.randint(0, 4)] for x in range(7)]
# arr = ['q', 'i', 'e', 'm', 'w', 'v', 'a', 'i', 'w', 'i', 'o', 'i']
random.shuffle(arr)
k = random.randint(3, 7)
# k = 3
print(arr)
print(k)
print(max_vowels())
