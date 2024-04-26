"""
3. Create an university enrollment system with the following characteristics:
* 		The system has a [login] with a username and password.
* 		Upon logging in, a [menu] displays the available [programs]: [1] Computer Science, [2] Medicine, [3] Marketing, and [4] Arts.
* 		The user must [input] their [1] first name, [2] last name, and [3] chosen program.
* 		Each [program] has only [5 available slots]. The system will [store the data of each registered user], and if it exceeds the limit, it should display a message indicating the program is unavailable.
* 		If [login] information is [incorrect three times], the system should be locked.
* 		The user must [choose a campus from three cities]: London, Manchester, Liverpool.
* 		In [London], there is 1 slot per program; in [Manchester], there are 3 slots per program, and in [Liverpool], there is 1 slot per program.
* 		If the user selects a program at a campus that has no available slots, the system should [display the option to enroll in the program at another campus].
"""

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

campus_db = {
    "LON": {
        "name": "London",
    },
    "MAN": {
        "name": "Manchester",
    },
    "LIV": {
        "name": "Liverpool"
    }
}  

programs_db = {
    "CSC": {
        "name": "Computer Science",
    },
    "MED": {
        "name": "Medicine",
    },
    "MKT": {
        "name": "Marketing",
    },
    "ART": {
        "name": "Arts",
    }
}        

slots_db = {
    "London": {
        "Computer Science": 1,
        "Medicine": 1,
        "Marketing": 1,
        "Arts": 1
    },
    "Manchester": {
        "Computer Science": 3,
        "Medicine": 3,
        "Marketing": 3,
        "Arts": 3
    },
    "Liverpool": {
        "Computer Science": 1,
        "Medicine": 1,
        "Marketing": 1,
        "Arts": 1
    }
}

students_data_db = {}



#title() receives a title and the desired number of spaces for a centered header  
def title(title, menu_min):
    menu_min_str = menu_min * " "
    menu_title = f'{menu_min_str}{title}{menu_min_str}'
    return menu_title


#menu_length() receives a dictionary containing the available programs to find the lengths that will be used in generating the menu. It also adjusts the title for a centered header.
def menu_length(db, header, menu_title):

    menu_codes_str = [] 
    menu_codes_len = []
    
    for key in db.keys():
        menu_code = f'[{key}] {db[key][header]}'
        menu_codes_str.append(menu_code)
        menu_codes_len.append(len(menu_code))

    max_menu_codes_len = max(menu_codes_len)
    if max_menu_codes_len % 2 == 0:
        pair_menu_codes_len = True
    else:
        pair_menu_codes_len = False
    

    menu_title_len = len(menu_title)
    if menu_title_len % 2 == 0:
        pair_menu_title_len = True
    else:
        pair_menu_title_len = False

    menu_title_ok = menu_title

    if pair_menu_codes_len != pair_menu_title_len:
        menu_title_ok = f'{menu_title} '
        menu_title_len = len(menu_title_ok)

    menu_len = []
    menu_len.append(max_menu_codes_len)
    menu_len.append(menu_title_len)
    menu_len = max(menu_len) +2 #I added two to account for the initial margin and the final margin.

    return menu_title_ok, menu_len, menu_title_len, menu_codes_str


#select_menu() generates the menu with the available programs using the lengths and list generated in the menu_length() function.
def select_menu(title, menu_len, menu_title_len, menu_codes_str):
    
    box = menu_len * "═"
    centered = int((menu_len - menu_title_len) /2) * " "

    print()
    print(f"╔{box}╗")
    print(f"║{centered}{title}{centered}║")
    print(f"╠{box}╣")
    
    items = len(menu_codes_str)

    for i in range(items):
        space = (menu_len - (len(menu_codes_str[i])) -1) * " "
        print(f"║ {menu_codes_str[i]}{space}║")
    
    print(f"╚{box}╝")


def login_fail(max_login_tries, tries):

    if tries != max_login_tries: 
        print('Invalid username or password. Please try again.')
        print('tries left: ' + str(max_login_tries - tries))
    else:
        print('Too many login attempts. Please try again later.\n')


def login(users_db, max_login_tries, auth):
    
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


#random_pick() generates fictitious data for random_users_db() by choosing a program and campus while respecting the available slots.
def random_pick(slots_db):
    
    chosen_campus = random.choice(list(slots_db.keys()))
    chosen_program = random.choice(list(slots_db[chosen_campus].keys()))

    while slots_db[chosen_campus][chosen_program] == 0:

        chosen_campus = random.choice(list(slots_db.keys()))
        chosen_program = random.choice(list(slots_db[chosen_campus].keys()))

    slots_db[chosen_campus][chosen_program] -= 1 #it updates the database
    return slots_db, chosen_program, chosen_campus


#random_users_db() generates fictitious data that is added to the students_data dictionary.
def random_users_db(slots_db):
    
    for i in range(1, random_students + 1):
        
        student_id = "S" + str(i)
        slots_db, random_program, random_campus = random_pick(slots_db)
        
        students_data_db[student_id] = {
            "first_name": random.choice(names),
            "last_name": random.choice(last_names),
            "chosen program": random_program,
            "campus": random_campus
            }
        
    return students_data_db


def update_students_data(students_data_db, name, last_name, chosen_program, chosen_campus):
    
    i = (len(students_data_db))+1
    student_id = "S" + str(i)

    students_data_db[student_id] = {
        "first_name": name,
        "last_name": last_name,
        "chosen program": chosen_program,
        "campus": chosen_campus
        }
        
    return students_data_db


#is_available() identifies if there are available slots in any of the campuses.
def is_available(chosen_program):
    
    is_available = []
    
    for key, value in slots_db.items():
        available_list = is_available.append(value[chosen_program])
        available_list = max(is_available)
    
    return available_list


def input_1(programs_db):
    
    code = str(input("\nEnter your program: ").upper())
    
    while code not in list(programs_db.keys()):
        print("Invalid. Please try again.\n")
        code = str(input("Enter your program: ").upper())

    choosen_program = programs_db[code]["name"]

    return choosen_program


def input_2(campus_db):
    
    code = str(input("\nEnter your campus: ").upper())
    
    while code not in list(campus_db.keys()):
        print("Invalid. Please try again.\n")
        code = str(input("Enter your campus: ").upper())
    
    choosen_campus = campus_db[code]["name"]
    
    return choosen_campus



#random_students determines the number of simulated students who have already chosen a program before the user.
random_students = 15
max_login_tries = 3
auth = False
names = ["James", "John", "Robert", "Michael", "William"]
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones"]



students_data_db = random_users_db(slots_db)
auth = login(users_db, max_login_tries, auth)

if auth == True:
    
    print()
    JSON_slots_db = json.dumps(slots_db, indent = 4)
    print(JSON_slots_db)
    print()
    print("Above, you'll find the list of available programs on each campus.")

    name = input("\n\nWelcome back!\nType your first name: ")
    last_name = input("Type your last name: ")

    menu_1_title = title("PROGRAMS", 8)
    menu_1_title_ok, menu_1_len, menu_1_title_len, menu_1_codes_str = menu_length(programs_db, "name", menu_1_title)
    select_menu(menu_1_title_ok, menu_1_len, menu_1_title_len, menu_1_codes_str)
    
    chosen_program = input_1(programs_db)
    
    menu_2_title = title("CAMPUS", 8)
    menu_2_title_ok, menu_2_len, menu_2_title_len, menu_2_codes_str = menu_length(campus_db, "name", menu_2_title)
    select_menu(menu_2_title_ok, menu_2_len, menu_2_title_len, menu_2_codes_str)
    
    chosen_campus = input_2(campus_db)

    slots_available = is_available(chosen_program)
    
    if slots_available != 0:

        while slots_db[chosen_campus][chosen_program] == 0:
            print("\nNo available slots here.\nTry again on other campus.")
            
            menu_2_title = title("CAMPUS", 8)
            menu_2_title_ok, menu_2_len, menu_2_title_len, menu_2_codes_str = menu_length(campus_db, "name", menu_2_title)
            select_menu(menu_2_title_ok, menu_2_len, menu_2_title_len, menu_2_codes_str)
    
            chosen_campus = input_2(campus_db)

        students_data_db = update_students_data(students_data_db, name, last_name, chosen_program, chosen_campus)
        
        JSON_students_data_db = json.dumps(students_data_db, indent = 4)
        print(JSON_students_data_db)

        slots_db[chosen_campus][chosen_program] -= 1 #it updates the database to remove the slot that the user just selected.

        print(f"\n\nSuccess!\nYou have successfully enrolled in {chosen_program} at the {chosen_campus} campus.\n")
    
    else: 
        print(JSON_slots_db)
        print("\nAbove, you'll find the list of programs that are still available\n\nProgram isn't available on any of the campuses.\nTry enrolling again in the next round of applications.\n")


