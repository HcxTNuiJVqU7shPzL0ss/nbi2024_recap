# pylint: skip-file
# noqa
#####################################################################
# Jan Berglund - e4_different_solution.py
#
# Veckouppgift 3
# Vecka 4, 20/1
# 4 Figurer med loopar
#####################################################################


from img_def import *


print('\nYou will be asked to input a character, or select all.')
input('\nPress enter to continue')


while True:
    user_inp = input('\nType a character "a-j", "all", or "q"'
                       ', then press enter.\n')
    user_inp = user_inp.lower()
    if len(user_inp) == 0:
        print('You just hit enter, try again!')
        continue
    elif user_inp in 'q':
        print('\n\nOK, quit with no action!')
        break
    else:
        if user_inp in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                        'i', 'j', 'all'):
            input_string = '\n...................."4.' + user_inp + '"....................\n'
            if user_inp in 'a':
                img_a(input_string)
            elif user_inp in 'b':
                img_b(input_string)
            elif user_inp in 'c':
                img_c(input_string)
            elif user_inp in 'd':
                img_d(input_string)
            elif user_inp in 'e':
                img_e(input_string)
            elif user_inp in 'f':
                img_f(input_string)
            elif user_inp in 'g':
                img_g(input_string)
            elif user_inp in 'h':
                img_h(input_string)
            elif user_inp in 'i':
                img_i(input_string)
            elif user_inp in 'j':
                img_j(input_string)
            else:
                input_string = '\nYou are running all!'
                img_a(input_string + ' --> a') , img_b(input_string + ' --> b')
                img_c(input_string + ' --> c') , img_d(input_string + ' --> d')
                img_e(input_string + ' --> e') , img_f(input_string + ' --> f')
                img_g(input_string + ' --> g') , img_h(input_string + ' --> h')
                img_i(input_string + ' --> i') , img_j(input_string + ' --> j')
            again_q = input('\n     ... Would you like to play again, hit "y"!\n')
            again_q = again_q.lower()
            if len(again_q) != 0 and again_q in 'y':
                print('\nwhopee, here we go again!')
                continue
            else:
                print('\nBoo...')
                break
        else:
            print('Selected input not valid!')
            print('Please try again...')
            continue


# End program
input('\nPress enter to finish!')
