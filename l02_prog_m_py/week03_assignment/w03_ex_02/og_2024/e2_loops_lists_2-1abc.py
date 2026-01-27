# pylint: skip-file
# noqa
#####################################################################
# Jan Berglund - e2_loops_lists_2-1abc.py
#
# Veckouppgift 3
# Vecka 4, 20/1
# 2 Öva på loopar och listor / 1a, 1b, 1c
#####################################################################


import sys


print("\nYou will be asked to select which part of the assignment "
      "to run:\na, b, or c.")
input("\nPress enter to continue")

# Wait for appropriate response from the user
while True:
    user_sel = input("\nSelect 'a', 'b' or 'c'"
                       ", then press enter.\n")
    user_sel = user_sel.lower()
    if user_sel in ("a", "b", "c"):
        break
    else:
        print("\nUnknown option, please try again!")
        continue


init_divider = '\n...................."2.1' + user_sel + '"....................'
init_print = '\nThis is the start of "2.1' + user_sel + '" part.'
init_continue = 'Press Enter to continue with "2.1' + user_sel + '"...\n'


####################################################
# Start of "2.1a" part of exercise
####################################################
if user_sel == 'a':
    print(init_divider)
    print(init_print)
    input(init_continue)

    """1a Skriv färdigt kodexemplet.
    answer = 0
    for i in ????????????:
        answer += i
    print("Summan av talen 1 till 10 är: " + str(answer))
    # Svaret ska bli 55
    
    JB comment: Will do some changes, as of
        a) will write things in English
        b) will do some edits where I feel it suits better"""

    # Initial declaration
    sum_tot = 0 # answer

    # Loop to calculate the answer of: 1 + 2 + ... + 10
    for i in range(1,11,1): # Start at 1, stop at (do not include) 11, step with 1
        sum_tot += i # Same as: sum_tot = sum_tot + i

    print('The sum of the numbers 1 through 10 is:', sum_tot)

    if sum_tot != 55:
        sys.exit('\nExpected sum to be 55, something has gone wrong!\n')


    ####################################################

    # Extra silly stuff

    check_silly = input("\nDo you want to continue with silly stuff?\n"
                        "If yes, press 'y' then enter, else just enter.\n")

    # Make sure both lower (y) and upper (Y) case is accepted
    check_silly = check_silly.lower()

    if check_silly != "y":
        print("\nNo worries, skip this!")
    else:
        end_int = 10
        silly_answer = 0

        print('\n\nSequence end integer "n" is' , end_int)
        print('Calculate as of ((n(n+1))/2)')

        silly_answer = ((end_int*(end_int+1))/2)
        print('Answer calculated is:', int(silly_answer))


        print('End of all the silly stuff as well\n')


####################################################
# Start of "2.1b" part of exercise
####################################################
elif user_sel == 'b':
    print(init_divider)
    print(init_print)
    input(init_continue)

    """
    1b Räkna ut summan av alla tal mellan 1 och 100. (inklusive 1 och 100, rätt svar ska bli 5050)
    """

    # Define the gaussian sum using a for loop
    def gaussian_sum_for(r_start,r_stop,r_step):
        # noqa
        sum_step = 0
        for i in range(r_start,r_stop,r_step):
            sum_step += i
        return sum_step

    start_for = 1
    stop_for = 100
    step_for = 1

    answer_for = gaussian_sum_for(start_for,(stop_for + 1),step_for)

    print('The sum of all integers from 1 to', stop_for, 'is:', answer_for)

    if answer_for != 5050:
        sys.exit('\nExpected sum to be 5050, something has gone wrong!\n')


####################################################
# Start of "2.1c" part of exercise
####################################################
elif user_sel == 'c':
    print(init_divider)
    print(init_print)
    input(init_continue)

    """
    1c Skriv om 1b så att den använder en while-loop.
    """

    # Define the gaussian sum using a while loop
    def gaussian_sum_while(r_start,r_stop,r_step):
        # noqa
        sum_step = 0
        i = r_start
        while i < r_stop:
            sum_step += i
            i += r_step
        return sum_step


    start_while = 1
    stop_while = 100
    step_while = 1

    answer_while = gaussian_sum_while(start_while,(stop_while + 1),step_while)

    print('The sum of all integers from 1 to', stop_while, 'is:', answer_while)

    if answer_while != 5050:
        sys.exit('\nExpected sum to be 5050, something has gone wrong!\n')


####################################################
# The end...
####################################################
else:
    sys.exit('\nThis should not be possible!\n')

input('\nPress Enter to finish this...\n')
