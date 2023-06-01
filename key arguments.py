def count_vowels(word):
    '''Is supposed to count vowels (except y) in a word'''
    vowels = "aeiou"
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1
    return count
count_vowels("able")