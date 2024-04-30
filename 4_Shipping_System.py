"""
4. Create an online shipping system with the following features:
* 		The system has a login that locks after the third failed attempt.
* 		Display a menu that allows: Sending a package, exiting the system.
* 		To send a package, sender and recipient details are required.
* 		The system assigns a random package number to each sent package.
* 		The system calculates the shipping price. $2 per kg.
* 		The user must input the total weight of their package, and the system should display the amount to pay.
* 		The system should ask if the user wants to perform another operation. If the answer is yes, it should return to the main menu. If it's no, it should close the system.
"""

import datetime
import random
import json


users_db = {
    "01": {
        "username": "Enrique",
        "password": "AcruBeast",
    },
    "02": {
        "username": "Daniela",
        "password": "Blindma1den",
    }
}

menu_options_1st = {
    "SEND": {
        "text": "Send a package",
    },
    "EXIT": {
        "text": "Exit the system",
    }
}

send_db = {}


def login_fail(max_login_tries, tries):

    if tries != max_login_tries: 
        print('Invalid username or password. Please try again.')
        print('tries left: ' + str(max_login_tries - tries))
    else:
        print('Too many login attempts. Please try again later.\n')


def login(users_db, max_login_tries = 3, auth = False):
    
    tries = 0
    
    while tries < max_login_tries:
        
        input_username = input('\nType your username: ')
        input_password = input('Type your password: ')
        print()

        for key, value in users_db.items(): #key, value indicates depth.
            if value["username"] == input_username and value["password"] == input_password:
                auth = True
    
        if auth == True:
            #print(f"Welcome back, {input_username}!")
            break
        else:
            tries += 1
            login_fail(max_login_tries, tries)

    return auth


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


def menu_title_1st(title = "TITLE", menu_min = 8):
    menu_min_str = menu_min * " "
    menu_title = f'{menu_min_str}{title}{menu_min_str}'

    menu_title_len = len(menu_title)

    return menu_title, menu_title_len


#Ajuste en el títlo en caso de que las opciones y el títulos no coincidan en si son par
def menu_title_2nd(bool_is_pair_options, title):

    menu_title, menu_title_len = menu_title_1st(title)
    bool_is_pair_title = is_pair(menu_title_len)
    
    menu_title_ok = menu_title
    menu_title_len_ok = menu_title_len #si no se cumple la condición, guarda el dato de menu_title_1st() sin aplicar cambios 
    if bool_is_pair_options != bool_is_pair_title:
        menu_title_ok = f'{menu_title} '
        menu_title_len_ok = len(menu_title_ok)

    return menu_title_ok, menu_title_len_ok


#comparación de los valores representativos para identificar el más grande y a ese sumar dos
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
    #cuando menu_len == menu_title_len_ok, resulta en uno porque a menu_len se le sumaron +2.

    print()
    print(f"╔{box}╗")
    print(f"║{centered}{menu_title_ok}{centered}║") #si son dos centered, se está sumado un espacio en blanco adicional tanto al inicio como al final en el título.
    print(f"╠{box}╣")
    
    items = len(menu_options_str)
    for i in range(items):
        space = (menu_len - (len(menu_options_str[i])) -1) * " " #quita de la cuenta el espacio en blanco adicional que se agrega al inicio con print(f"║ {...}║").
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


def form_1(ask_txt_1, ask_txt_2):

    while True:
        
        ask_input_1 = f'\n{ask_txt_1} '
        ask_input_2 = f'{ask_txt_2} '        
        
        user_input_1 = input(ask_input_1)
        user_input_2 = input(ask_input_2)

        user_confirmation = input('\nIs this information accurate? Y/N ').upper()

        while user_confirmation not in ['Y', 'N']:
            print('Please enter Y or N.')
            user_confirmation = input('Is this information accurate? Y/N ').upper()

        if user_confirmation == 'Y':
            print('Information saved.')
            break

    return user_input_1, user_input_2


def form_2(ask_txt_1):
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


def shipping_price(package_weight, price):

    amount = package_weight * price
    print(f'\nThe weight of your package is {package_weight} kg, the amount to be paid is {amount} USD.')

    return amount


def add_to_db(send_db, sender_name, sender_address, recipient_name, recipient_address, package_weight, selling_price):
    
    user_confirmation = input('Would you like to proceed with the shipping? Y/N ').upper()

    while user_confirmation not in ['Y', 'N']:
        print('Please enter Y or N.')
        user_confirmation = input('Would you like to proceed with the shipping? Y/N ').upper()

    if user_confirmation == 'N':
        send_id = "S/N"
        return False, send_db, send_id

    elif user_confirmation == 'Y':

        i = (len(send_db))+1
        send_id = "S" + str(i)

        date_time_now_1 = datetime.datetime.now()
        date_time_now_2 = date_time_now_1.strftime("%Y%m%d%H%M%S")
        random_number = random.randint(1, 100)
        random_tracking_number = str(random_number) + '-' + str(date_time_now_2)

        send_db = {
            "sender_name": sender_name,
            "sender_address": sender_address,
            "recipient_name": recipient_name,
            "recipient_address": recipient_address,
            "package_weight": package_weight,
            "selling_price": selling_price,
            "random_tracking_number": random_tracking_number,
        }
        
        print('\nSuccessful transaction, please proceed to one of our offices to deliver your package.')
        return True, send_db, send_id
    



auth = login(users_db)
if auth == True:
    while True:

        menu_options_str, menu_title_ok, menu_title_len_ok, menu_len = menu_length(menu_options_1st, "text","SELECT")
        select_menu(menu_options_str, menu_title_ok, menu_title_len_ok, menu_len)
        user_selection = input_1("Type your selection:", "Invalid. Please try again.", list(menu_options_1st.keys()))

        if user_selection == 'EXIT':
            break
        elif user_selection == 'SEND':
            sender_name, sender_address = form_1('Type sender full name:', 'Type sender address:')
            recipient_name, recipient_address = form_1('Type recipient full name:', 'Type recipient address:') 
            package_weight = form_2('Type package weight in kilograms:')
            selling_price = shipping_price(package_weight, 2)
            save, new_item, send_id = add_to_db(send_db, sender_name, sender_address, recipient_name, recipient_address, package_weight, selling_price)
            
            if save == True:
                send_db[send_id] = new_item

        user_confirmation = input('\nWould you like to perform another operation? Y/N ').upper()
        
        while user_confirmation not in ['Y', 'N']:
            print('Please enter Y or N.')
            user_confirmation = input('\nWould you like to perform another operation? Y/N ').upper()

        if user_confirmation == 'N':
            break

    JSON_send_db = json.dumps(send_db, indent = 4)
    print(JSON_send_db)
