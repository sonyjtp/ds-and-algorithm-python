# https://tinyurl.com/leetcode007

def check_if_pangram():
    letter_count = {}
    distinct_letters = 0
    for letter in sentence:
        if letter in letter_count:
            continue
        letter_count[letter] = 1
        distinct_letters += 1
        if distinct_letters == 26:
            return True
    return False


sentence = "thequickbrownfoxjumpsoverthelazydog"
print(sentence)
print(check_if_pangram())
