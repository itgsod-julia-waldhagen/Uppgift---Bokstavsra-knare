import string

def count_letters(word):
    word = word.lower()
    letter_dict = {}
    white = string.whitespace
    for letter in word:
        if letter not in white:
            if letter in letter_dict:
                letter_dict[letter]+=1
            else:
                letter_dict[letter] = 1
    return letter_dict


count_letters("hello")




