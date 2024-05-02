"""
5. Develop a finance management application with the following features:
* 		The user records their [total income].
* 		There are [categories]: [1] Medical expenses, [2] household expenses, [3] leisure, [4] savings, and [5] education.
* 		The user can [list their expenses] within the categories and get the [total for each category].
* 		The user can obtain the [total of their expenses].
* 		[If] the user [spends the same] amount of money they earn, the system should display a [message advising] the user to reduce expenses in the category [where] they have spent the most money.
* 		[If] the user [spends less] than they earn, the system displays a [congratulatory message] on the screen.
* 		[If] the user [spends more] than they earn, the system will display [advice to improve] the user's financial health.
"""
import json

menu_options_1st = {
    "MED": {
        "name": "Medical",
    },
    "HSE": {
        "name": "Household",
    },
    "LEI": {
        "name": "Leisure",
    },
    "EDU": {
        "name": "Education"
    },
    "SAV": {
        "name": "Savings"
    }
}


menu_options_2nd = {
    "1": {
        "name": "Add another expense in this category",
    },
    "2": {
        "name": "Change category",
    },
    "3": {
        "name": "Finish and view results",
    }
}


def is_pair(len): 
    if len % 2 == 0:
        bool_len = True
    else:
        bool_len = False

    return bool_len


def menu_options_list(dictionary, header):

    menu_options_str = [] 
    menu_options_len = []
    
    for key in dictionary.keys():
        menu_option = f'[{key}] {dictionary[key][header]}'
        menu_options_str.append(menu_option)
        menu_options_len.append(len(menu_option))

    menu_options_len_max = max(menu_options_len)
    bool_is_pair_options = is_pair(menu_options_len_max)
    
    return menu_options_str, menu_options_len_max, bool_is_pair_options 


def menu_title_1st(title = "TITLE", menu_min = 4):
    menu_min_str = menu_min * " "
    menu_title = f'{menu_min_str}{title}{menu_min_str}'

    menu_title_len = len(menu_title)

    return menu_title, menu_title_len


def menu_title_2nd(bool_is_pair_options, title):

    menu_title, menu_title_len = menu_title_1st(title)
    bool_is_pair_title = is_pair(menu_title_len)
    
    menu_title_ok = menu_title
    menu_title_len_ok = menu_title_len 
    if bool_is_pair_options != bool_is_pair_title:
        menu_title_ok = f'{menu_title} '
        menu_title_len_ok = len(menu_title_ok)

    return menu_title_ok, menu_title_len_ok


def menu_length(dictionary, header, title):

    menu_options_str, menu_options_len_max, bool_is_pair_options = menu_options_list(dictionary, header)
    
    menu_title_ok, menu_title_len_ok = menu_title_2nd(bool_is_pair_options, title)

    menu_len = []
    menu_len.append(menu_options_len_max) 
    menu_len.append(menu_title_len_ok) 
    menu_len = max(menu_len) +2 #I added two to account for the initial blank margin and the final margin blank.

    return menu_options_str, menu_title_ok, menu_title_len_ok, menu_len


#select_menu() generates the menu with the available options using the lengths and list generated in the menu_length() function.
def select_menu(menu_options_str, menu_title_ok, menu_title_len_ok, menu_len):
    
    box = menu_len * "═"
    centered = int((menu_len - menu_title_len_ok) /2) * " "

    print()
    print(f"╔{box}╗")
    print(f"║{centered}{menu_title_ok}{centered}║") 
    print(f"╠{box}╣")
    
    items = len(menu_options_str)
    for i in range(items):
        space = (menu_len - (len(menu_options_str[i])) -1) * " " 
        print(f"║ {menu_options_str[i]}{space}║") 
    
    print(f"╚{box}╝")


def input_1(ask_txt, error_txt, in_list):
    
    ask_input = f'\n{ask_txt} '
    print_error = f'\n{error_txt}'

    user_input = input(ask_input).upper()

    while user_input not in list(in_list):
        print(print_error)
        user_input = input(ask_input).upper()
    
    return user_input

def input_isfloat(ask_txt_1):
    while True:
        user_input_1 = input(f'\n{ask_txt_1} ')
        
        try:
            user_input_1 = float(user_input_1)
            break
        except ValueError:
            print('Please enter a valid number.')

    while True:
        user_confirmation = input('\nIs this information accurate? Y/N ').upper()

        if user_confirmation == 'Y':
            print('Information saved.')
            break
        elif user_confirmation == 'N':
            while True:
                user_input_1 = input(f'\n{ask_txt_1} ')

                try:
                    user_input_1 = float(user_input_1)
                    break
                except ValueError:
                    print('Please enter a valid number.')
        else:
            print('Please enter Y or N.')

    return user_input_1


def ask_1(ask_txt_1):

    while True:
        
        ask_input_1 = f'\n{ask_txt_1} '     
        
        user_input_1 = input(ask_input_1)

        user_confirmation = input('\nIs this information accurate? Y/N ').upper()

        while user_confirmation not in ['Y', 'N']:
            print('Please enter Y or N.')
            user_confirmation = input('Is this information accurate? Y/N ').upper()

        if user_confirmation == 'Y':
            print('Information saved.')
            break

    return user_input_1


def update_db(db, category, description, cost):
    
    record_id = len(db[category])+1
    db[category][record_id] = {
        "description": description,
        "cost": cost
    }

    return db


def create_dictionary(db):
    
    new_db = {}

    for i in db:
        new_db[i] = {}

    return new_db


def add_expense(category, production_db, user_selection_1, menu_options_2nd):
    
    while True:
        print(f"You've chosen to record your annual expenses in the {category} category. Please enter each one below.")
        description = ask_1('Expense Description:')
        cost = input_isfloat('Annual Cost:')

        production_db = update_db(production_db, user_selection_1, description, cost)

        menu_options_str, menu_title_ok, menu_title_len_ok, menu_len = menu_length(menu_options_2nd, "name","SELECT")
        select_menu(menu_options_str, menu_title_ok, menu_title_len_ok, menu_len)

        user_selection_2 = input_1("Type your selection:", "Invalid. Please try again.", list(menu_options_2nd.keys()))
    
        if user_selection_2 != '1':
            break
    
    return production_db, user_selection_2


def total_cost(db_key, db):

    cost_list = []

    cost_max_1st = 0
    cost_max_2nd = 0

    for key in list(db_key.keys()):
        for i in range(1, len(db[key]) + 1):
            cost = db[key][i]["cost"]
            cost_list.append(cost)

            if cost > cost_max_1st:
                cost_max_2nd = cost_max_1st
                cost_max_1st = cost
                
            elif cost > cost_max_2nd and cost != cost_max_1st:
                cost_max_2nd = cost

    total_cost = sum(cost_list)

    return total_cost, cost_max_1st, cost_max_2nd


def category_cost(db, key):
    
    cost_list = []
    
    for i in range(1, len(db[key]) + 1):
        cost = db[key][i]["cost"]
        cost_list.append(cost)

    total_category_cost = sum(cost_list)
    
    return total_category_cost


def print_same_cost(options_db, info_db, amount):

    for key in list(options_db.keys()):
        for i in range(1, len(info_db[key]) + 1):
            k = key
            items = info_db[key]
            if items[i]["cost"] == amount:
                print(f"${amount} {items[i]['description'].capitalize()}, within category: {k}")




production_db = create_dictionary(menu_options_1st)
print("\nWelcome to my finance management system!\nLet's start by recording your annual income, and then proceed to record your annual expenses divided into categories.")
income = input_isfloat("Type your annual income: ")

while True:

    menu_options_str, menu_title_ok, menu_title_len_ok, menu_len = menu_length(menu_options_1st, "name","EXPENSE CATEGORIES")
    select_menu(menu_options_str, menu_title_ok, menu_title_len_ok, menu_len)

    user_selection_1 = input_1("Type your selection:", "Invalid. Please try again.", list(menu_options_1st.keys()))
    category = menu_options_1st[user_selection_1]["name"].upper()

    production_db, user_selection_2 = add_expense(category, production_db, user_selection_1, menu_options_2nd)

    if user_selection_2 == '3':
        break
cost_all, cost_max_1st, cost_max_2nd = total_cost(menu_options_1st, production_db) 


category_cost_db = create_dictionary(menu_options_1st)
for key in list(menu_options_1st.keys()):
    category_cost_db[key] = category_cost(production_db, key)   
costly_category = max(category_cost_db, key=category_cost_db.get)


JSON = json.dumps(production_db, indent = 4)
print(JSON)


if income == cost_all:
    print(f"\nCurrently, you're spending as much as you're earning.")
    print(f"Consider reviewing your expenses in category {menu_options_1st[costly_category]['name'].upper()}, as it appears to be the most costly, accounting for ${category_cost_db[costly_category]} of your budget.\n")

elif income < cost_all:
    print(f"\nCurrently, you're spending more than you're earning!!")
    print(f"Consider reviewing your expenses in category {menu_options_1st[costly_category]['name'].upper()}, as it appears to be the most costly, accounting for ${category_cost_db[costly_category]} of your budget.")
    print(f"\nAlso, review the following expenses, which have been identified as the most costly:")
    print_same_cost(menu_options_1st, production_db, cost_max_1st)
    if cost_max_2nd > 0:
        print_same_cost(menu_options_1st, production_db, cost_max_2nd)

else:
    print("\nCongratulations! Your financial discipline is commendable as you're spending less than you earn. Keep up the great work!\n")














