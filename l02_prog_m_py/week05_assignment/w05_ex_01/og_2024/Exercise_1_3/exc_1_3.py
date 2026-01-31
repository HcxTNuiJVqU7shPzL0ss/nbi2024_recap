# pylint: skip-file
# noqa
# Exercise 1.3
# Jan Berglund


def count_vowels(word):
    # noqa
    vowels_cnt = 0
    word_lower = word.lower()
    vowels = "aeiou"
    for letter in word_lower:
        if letter in vowels:
            vowels_cnt += 1
    return vowels_cnt
