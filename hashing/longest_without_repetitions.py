# https://tinyurl.com/leetcode018


def longest_without_repetitions():
    letter_set = set()
    l, r, longest = (0, 0, 0)
    for r in range(len(s)):
        while s[r] in letter_set:
            letter_set.remove(s[l])
            l += 1
        letter_set.add(s[r])
        longest = max(longest, r - l + 1)
    return longest


s = 'abcabcdabcdeababcdefg ababc'
print(longest_without_repetitions())
