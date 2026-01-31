# pylint: skip-file
# noqa
# Exercise 1.2
# Jan Berglund


# Returns the sum of any numbers in the list
def sum_list(list):
    # noqa
    sum = 0
    for item in list:
        try:
            isinstance(item, float)
            sum += float(item)
        except ValueError:
            try:
                isinstance(item, int)
                sum += int(item)
            except ValueError:
                continue
    return sum
