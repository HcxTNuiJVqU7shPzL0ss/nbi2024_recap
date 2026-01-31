# pylint: skip-file
# noqa


def c_t_f(degree):
    # noqa
    if degree < -273.15:
        return None
    return round((degree * 9 / 5 + 32), 1)


def count_words(sentence):
    # noqa
    cnt_wrd = 0
    if not sentence:
        return None
    else:
        cnt_wrd = (sentence.count(" ")) + 1
    return cnt_wrd
