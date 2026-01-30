# pylint: skip-file
# noqa
# print("\033[4mhello\033[0m")

todo_list = []
done_list = []

while True:
    print('\n\033[4mToDo List:\033[0m\n'
          '1: Print your list\n'
          '2: Add new things to your list\n'
          '3: Mark as "Done"\n'
          '4: Remove "Done" (add back)\n'
          'q: Quit (end program, list is gone)\n')
    option = input('Select an option from the menu: ')
    if option == '1':
        if len(todo_list) == 0:
            print('\nYour list is empty!')
            input('Press Enter to go back to menu...')
            continue
        else:
            i = 0
            for todo in todo_list:
                print(str(i) + ' ' + todo)
                i += 1
            input('Press Enter to go back to menu...')
            continue
    elif option == '2':
        add_todo = input('\nEnter what is to be added to the list: ')
        todo_list.append(add_todo)
        input('Press Enter to go back to menu...')
        continue
    elif option == '3':
        try:
            done_todo = int(input('Which index in your list are you done with?\n'))
            try:
                swap = todo_list[done_todo]
                done_list.append(swap)
            except:
                print('Could not find this...')
            input('Press Enter to go back to menu...')
        except ValueError:
            print("\nNot an integer!\n")
            input('Press Enter to go back to menu...')
            continue
    elif option == '4':
        if len(done_list) == 0:
            print('\nYour list is empty!')
            input('Press Enter to go back to menu...')
            continue
        else:
            i = 0
            for item in done_list:
                print(str(i) + ' ' + item)
                i += 1
            input('Press Enter to go back to menu...')
            continue
    elif option == 'q':
        print('\nOK, will quit!')
        quit()
    else:
        print('\nUnfamiliar option, try again!')
        input('Press Enter to go back to menu...')
        continue

print('All done!')
