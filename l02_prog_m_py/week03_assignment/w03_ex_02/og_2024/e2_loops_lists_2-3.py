# pylint: skip-file
# noqa
#####################################################################
# Jan Berglund - e2_loops_lists_2-3.py
#
# Veckouppgift 3
# Vecka 4, 20/1
# 2 Öva på loopar och listor / 3
#####################################################################


print('\nThis is the start of "2.3".')
input("Press enter to continue\n")

"""
3 Träna på att skapa och manipulera listor.
    Alla uppgifter ska lösas med funktionerna som står i presentationen.
3a Skapa en lista med namnen på fyra filmer. Namnen ska vara strängar.
    Skriv ut hela listan 2med funktionen print.
3b Lägg till "Fellowship of the ring" sist i listan.
3c Lägg till "The two towers" på första platsen i listan. (index noll)
3d Ta reda på vilken position (index) "Fellowship of the ring" har nu.
3e Ta bort en annan av filmerna. Har Fellowship-filmen ändrat index?
3f Ta reda på hur lång listan är. (len)
3g Vänd listan baklänges.
3h Sortera listan stigande i bokstavsordning.
"""


####################################################
# Start of "2.3a" part of exercise
####################################################

# 3a Skapa en lista med namnen på fyra filmer.
# Namnen ska vara strängar.
# Skriv ut hela listan 2med funktionen print.

print('\n...................."2.3a"....................')

# Skapa en lista med namnen på fyra filmer
# Namnen ska vara strängar
film_list = ['Pulp Fiction', 'Excalibur', 'Blade', 'Predator']

# Skriv ut hela listan 2med funktionen print
print('\nThe list of films is:', film_list)
print('\nThe films one by one are:')
for element in range(len(film_list)):
    print('[' + str(element) + ']', film_list[element])

input("\nPress enter to continue\n")


####################################################
# Start of "2.3b" part of exercise
####################################################

# 3b Lägg till "Fellowship of the ring" sist i listan.

print('\n...................."2.3b"....................')

# Add "Fellowship of the ring" to the end of the list
film_list.append('Fellowship of the Ring')

print('\nLast index in the list is now:', film_list[-1])

input("\nPress enter to continue\n")


####################################################
# Start of "2.3c" part of exercise
####################################################

# 3c Lägg till "The two towers" på första platsen
# i listan. (index noll)

print('\n...................."2.3c"....................')

film_list.insert(0, 'The Two Towers')
print('\nThe list of films is:', film_list)

input("\nPress enter to continue\n")


####################################################
# Start of "2.3d" part of exercise
####################################################

# 3d Ta reda på vilken position (index)
# "Fellowship of the ring" har nu.

print('\n...................."2.3d"....................')

# Find the index
for_index = film_list.index('Fellowship of the Ring')

print('\nThe film "Fellowship of the Ring" is now at '
      'index:', for_index)

input("\nPress enter to continue\n")


####################################################
# Start of "2.3e" part of exercise
####################################################

# 3e Ta bort en annan av filmerna.
# Har Fellowship-filmen ändrat index?

print('\n...................."2.3e"....................')

# Remove index '1' (Pulp Fiction)
film_list.pop(1)
for_index = film_list.index('Fellowship of the Ring')
print('\nThe film "Fellowship of the Ring" is now at '
      'index:', for_index)

print('\nThe list of films is:', film_list)

input("\nPress enter to continue\n")


####################################################
# Start of "2.3f" part of exercise
####################################################

# 3f Ta reda på hur lång listan är. (len)

print('\n...................."2.3f"....................')

print('\nThe length of the list is:', len(film_list))

input("\nPress enter to continue\n")


####################################################
# Start of "2.3g" part of exercise
####################################################

# 3g Vänd listan baklänges.

print('\n...................."2.3g"....................')

print('\nThe list of films is:', film_list)
print('Reversing order, please wait...')
film_list.reverse()
print('The list of films in reverse index order is:', film_list)

input("\nPress enter to continue\n")


####################################################
# Start of "2.3h" part of exercise
####################################################

# 3h Sortera listan stigande i bokstavsordning.

print('\n...................."2.3h"....................')

film_list.sort()

print('\nThe list of films sorted as ascending is:', film_list)

input("\nPress enter to exit...\n")
