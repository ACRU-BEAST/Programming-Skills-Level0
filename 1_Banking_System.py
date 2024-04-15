'''
1. Create an online [banking system] with the following features:

* Users must be able to [log in] with a username and password.
* If the user enters the wrong credentials [three times], the system must [lock them out].
* The initial [balance] in the bank account is [$2000].
* The system must allow users to [1] deposit, [2] withdraw, [3] view, and [4] transfer money.
* The system must [display a menu] for users to perform transactions.
'''

user_db = 'Acru-Beast'
password_db = 'P455W0RD'
max_tries = 3
operation = 0

balance = 2000
in_transit = 0

def error(max_tries, tries):
    if tries != max_tries: 
        print('Invalid username or password. Please try again.')
        print('tries left: ' + str(max_tries - tries))
    else:
        print('Too many login attempts. Please try again later.\n')

def credentials(user_db, password_db, max_tries):
    tries = 0

    while tries < max_tries:

        user = input('\nType your username: ')
        password = input('Type your password: ')
        print()

        if user != user_db or password != password_db:
            tries += 1
            error(max_tries, tries)
        else:
            print('Welcome Back\n')

def menu():
    print("╔════════════════════════╗")
    print("║          MENU          ║")
    print("╠════════════════════════╣")
    print("║ [1] Deposit            ║")
    print("║ [2] Withdraw           ║")
    print("║ [3] View Balance       ║")
    print("║ [4] Transfer Money     ║")
    print("║ [5] Exit               ║")    
    print("╚════════════════════════╝")
    print()

def deposit():
    global balance
    deposit = int(input('\nHow much would you like to deposit?: '))
    balance = balance + deposit
    print("╔════════════════════════╗")
    print("║       SUCCESSFUL       ║")
    print("╠════════════════════════╣")
    print('║ New balance: $' + str(balance))  
    print("╚════════════════════════╝")
    print()
    return deposit

def withdraw():
    global balance
    withdraw = int(input('\nHow much would you like to withdraw?: '))
    new_balance = balance - withdraw
    
    if new_balance < 0:
        print('Insufficient funds. Try again.')
        menu_logic(2)
    else:
        balance = balance - withdraw
        print("╔════════════════════════╗")
        print("║       SUCCESSFUL       ║")
        print("╠════════════════════════╣")
        print('║ New balance: $' + str(balance))  
        print("╚════════════════════════╝")
        print()

def view_balance(balance):
    print("╔════════════════════════╗")
    print("║       MY BALANCE       ║")
    print("╠════════════════════════╣")
    print('║ $' + str(balance))  
    print("╚════════════════════════╝")

def transfer_money():
    global balance
    global in_transit
    transfer = int(input('\nHow much would you like to transfer?: '))
    new_balance = balance - transfer

    if new_balance < 0:
        print('Insufficient funds. Try again.')
        menu_logic(4)
    else:
        beneficiary = int(input('\nType the beneficiary bank account number: '))
        balance = balance - transfer
        in_transit = in_transit - transfer
        print("╔════════════════════════╗")
        print("║       SUCCESSFUL       ║")
        print("╠════════════════════════╣")
        print('║ New balance: $' + str(balance))  
        print("╚════════════════════════╝")
        print()

def menu_logic(operation):
    if operation == 1:
        deposit()
    elif operation == 2:
        withdraw()
    elif operation == 3:
        view_balance(balance)
    elif operation == 4:
        transfer_money()
    elif operation == 5:
        print('\nExiting...')
    else:
        print('\nError: Invalid operation number. Try again.\n')   

#credentials(user_db, password_db, max_tries)
menu()
while operation != 5:
    operation = int(input('Type the operation number you wish to perform: '))
    menu_logic(operation)



