# https://tinyurl.com/leetcode015


def max_number_of_balloons():
    letter_dict = {'a': 0, 'b': 0, 'l': 0, 'o': 0, 'n': 0}
    for letter in word:
        if letter in 'ablon':
            letter_dict[letter] += 1
    return min(letter_dict['b'], letter_dict['a'],
               letter_dict['l'] // 2, letter_dict['o'] // 2,
               letter_dict['n'])


word = input()
print(word)
print(f'Max no. of balloons: {max_number_of_balloons()}')
