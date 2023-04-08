# https://tinyurl.com/leetcode017

def num_jewels_in_stones():
    jewel_count = 0
    for jewel in jewels:
        jewel_count += stones.count(jewel)
    return jewel_count


jewels = 'aA'
stones = 'aAAbbbb'
print(num_jewels_in_stones())
