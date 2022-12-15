print('main.py has executed.')
import random
list_num_max_const = 25
list_num_max_digits_const = 999



list_of_num = random.sample(range(1,list_num_max_digits_const), list_num_max_const)
print('Generating a list of ' + str(list_num_max_const) + ' numbers between 1 and ' +  str(list_num_max_digits_const))
print(list_of_num)


while True:
    try:
        sort_selection = str(input('Which sorting type would you like to use? Ascending, Descending, or none at all?: '))
    except ValueError:
        print("USER INPUT ERROR: Please enter a string of text. Ascending, Descending, or None")
        continue
    else:
        break

sort_selection_str = str(sort_selection)
print('User entered: ' + sort_selection_str)

sort_selection_str_first_digit = sort_selection_str[0:1]
print(sort_selection_str_first_digit)

if sort_selection_str_first_digit == 'd' or sort_selection_str_first_digit == 'D':
    print('User has selected Descending sorting option.')
    list_of_num.sort(reverse=True)
    print(list_of_num)
    sort_selection = 'DESC'
if sort_selection_str_first_digit == 'a' or sort_selection_str_first_digit == 'A':
    print('User has selected Ascending sorting option. Display list of numbers from lowest to highest')
    list_of_num.sort()
    print(list_of_num)
    sort_selection = 'ASC'
if sort_selection_str_first_digit == 'n' or sort_selection_str_first_digit == 'N':
    print('User has selected None sorting option. Displaying list of numbers without sorting.')
    print(list_of_num)
    sort_selection = 'NONE'

if not sort_selection == 'NONE' and not sort_selection == 'ASC' and not sort_selection == 'DESC':
    print('Incorrect sort option selected. Program has failed to execute.')