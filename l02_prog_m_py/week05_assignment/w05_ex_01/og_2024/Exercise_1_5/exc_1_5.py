# pylint: skip-file
# noqa
# Exercise 1.5
# Jan Berglund


# Finds the second largest integer in a list
# Empty list, or list with only one element
# returns "None"
def find_2nd_max(list_in):
    # noqa
    max_fnd = None
    sec_max = None
    if not list_in:
        return None
    elif len(list_in) == 1:
        return None
    else:
        for element in list_in:
            if max_fnd == None:
                max_fnd = element
                sec_max = float('-inf')
            elif element > max_fnd:
                sec_max = max_fnd
                max_fnd = element
            elif element > sec_max and element != max_fnd :
                sec_max = element
    return sec_max
