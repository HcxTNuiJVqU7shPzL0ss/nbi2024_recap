# pylint: skip-file
# noqa
#####################################################################
# Jan Berglund - e2_loops_lists_2-2.py
#
# Veckouppgift 3
# Vecka 4, 20/1
# 2 Öva på loopar och listor / 2
#####################################################################


print('\nThis is the start of "2.2".')
input("Press enter to continue\n")

"""
2 Räkna ut summan av alla elementen i listan: [1, -2, 3, -2, 4, -3]
"""

print('You will be asked to select between verbose or '
      'compact.')
input("\nPress enter to continue")

# Wait for appropriate response from the user
while True:
    user_sel = input('\nSelect "v" or "c"'
                       ", then press enter.\n")
    user_sel = user_sel.lower()
    if user_sel in ("v", "c"):
        break
    else:
        print("\nUnknown option, please try again!")
        continue

# Initial declarations
input_list =  [1, -2, 3, -2, 4, -3]
sum_total = 0
output_list = []

# Calculate the sum of the individual elements in the input list
for element in range(len(input_list)):
    # Save calculations to display later, if wanted
    output_list.append((str(sum_total) + ' + ' + str(input_list[element]) +\
                            ' = ' + str(sum_total + input_list[element])))
    # Verbose output
    if user_sel == 'v':
        print('\nList is:', input_list)
        print('Index is:', element)
        print('Value for index in list is:', input_list[element])
        print('Previous value was:', sum_total)
        print(sum_total, '+', input_list[element], '=', \
              (sum_total + input_list[element]))
        input("Press enter to continue")

    # Running sum calculation
    sum_total += input_list[element]

print('\nThe sum of the elements in the list' , input_list , \
      'is:' , sum_total , '\n')

# Verbose output
if user_sel == 'v':
    input("Press enter to continue\n")
    print('Calculations as of:')
    for element in range(len(output_list)):
        print(element , ':' , output_list[element])

input('\nPress Enter to finish this...\n')
