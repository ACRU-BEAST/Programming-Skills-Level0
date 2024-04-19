'''
2. Create a currency converter between [CLP, ARS, USD, EUR, TRY, GBP] with the following features:
* 		The [user must choose] their [initial currency] and the [currency they want to exchange] to.
* 		The [user can choose whether or not to withdraw] their funds. If they choose not to withdraw, it should [return to the main menu].
* 		If the user decides to withdraw the funds, the system will [charge a 1% commission].
* 		Set a [minimum and maximum amount for each currency], it can be of your choice.
* 		The system should [ask the user if they want to perform another operation]. If they choose to do so, it should restart the process; otherwise, the system should close.
'''

class Currency():
    def __init__(self, currency_code="Unknown", currency_name="Unknown", currency_value=0.0, currency_minimum=0, currency_maximum=0, currency_name_length=" "*1):
        self.code = str(currency_code)
        self.name = str(currency_name)
        self.value = float(currency_value)
        self.min = int(currency_minimum)
        self.max = int(currency_maximum)
        self.len = str(currency_name_length)
        
    def __call__(self):
        print(f"║ [{self.code}] {self.name} {self.len} ║")
    
#input_2() condition
to_currency_code = "Unknown" 
#while condition
done = "NO"

#commission fee
slice = 0.01

#date: 18/04/24
#unitconverters[.]net/currency-converter.html
#investing[.]com/currency-converter/
CLP = Currency("CLP", "Chilean peso", 0.0010215235, 1000, 1450000, " "*3)
ARS = Currency("ARS", "Argentine peso", 0.001150417, 900,1300000, " "*1)
USD = Currency("USD", "American dollar", 1.00, 1, 1500, " "*0)
EUR = Currency("EUR", "Euro", 1.0685278998, 1, 2300, " "*11)
TRY = Currency("TRY", "Turkish lira", 0.0307472063, 35, 50000, " "*3)
GBP = Currency("GBP", "Pound sterling", 1.247170482, 1, 2000, " "*1)

currencies_data = {
    CLP.code: {
        "name": CLP.name,
        "value": CLP.value,
        "min": CLP.min,
        "max": CLP.max,
        "len": CLP.len
    },
    ARS.code: {
        "name": ARS.name,
        "value": ARS.value,
        "min": ARS.min,
        "max": ARS.max,
        "len": ARS.len
    },
    USD.code: {
        "name": USD.name,
        "value": USD.value,
        "min": USD.min,
        "max": USD.max,
        "len": USD.len
    },
    EUR.code: {
        "name": EUR.name,
        "value": EUR.value,
        "min": EUR.min,
        "max": EUR.max,
        "len": EUR.len
    },
    TRY.code: {
        "name": TRY.name,
        "value": TRY.value,
        "min": TRY.min,
        "max": TRY.max,
        "len": TRY.len
    },
    GBP.code: {
        "name": GBP.name,
        "value": GBP.value,
        "min": GBP.min,
        "max": GBP.max,
        "len": GBP.len
    }
}

def select_menu():
    print()
    print("╔════════════════════════╗")
    print("║     CURRENCYS MENU     ║")
    print("╠════════════════════════╣")
    CLP()
    ARS()
    USD()
    EUR()
    TRY()
    GBP()
    print("╚════════════════════════╝")


def input_1():
    
    from_currency_code = str(input("\nEnter your currency: ").upper())
    
    while from_currency_code not in (CLP.code, ARS.code, USD.code, EUR.code, TRY.code, GBP.code):
        print("Invalid currency code. Please try again.\n")
        from_currency_code = str(input("Enter your currency: ").upper())
    return from_currency_code

def input_2():
   
    to_currency_code = str(input("\nEnter the currency you want to exchange to: ").upper())
    
    while to_currency_code not in (CLP.code, ARS.code, USD.code, EUR.code, TRY.code, GBP.code):
        print("Invalid currency code. Please try again.\n")
        to_currency_code = str(input("Enter your initial currency: ").upper())
    return to_currency_code

def input_3(from_currency_code):
    
    amount = float(input("\nEnter the amount to convert: "))
    
    while amount > currencies_data[from_currency_code]["max"] or amount < currencies_data[from_currency_code]["min"]:
        print(f'Amount can not be below {currencies_data[from_currency_code]["min"]} or above {currencies_data[from_currency_code]["max"]}. Please try again.\n')
        amount = float(input("Enter the amount to convert: "))
    return amount

def convert(amount, from_currency, to_currency):
    amount_usd = amount * from_currency
    converted_amount = amount_usd / to_currency
    return converted_amount

def income(converted_amount, slice):
    commission = converted_amount * slice
    return commission

def confirm(amount, from_currency_name, converted_amount, to_currency_name, commission, withdraw_amount): 
    
    global done
    proceed = "Unknown"
    repeat = "Unknown"

    print(f"\n{amount} {from_currency_name} is equal to {round(converted_amount,2)} {to_currency_name}\nWould you like to proceed? A commission fee of {round(commission,2)} {to_currency_name} [1%] will apply\n")
    
    while proceed not in ["Y", "N"]:
        
        proceed = input("Please type [Y] to confirm or [N] to decline: ").upper()
        print()

    if proceed == "Y":
        print(f'You have successfully withdrawn {round(withdraw_amount,2)} {to_currency_name}\n')
        
        while repeat not in ["Y", "N"]:
            
            repeat = input("Would you like to perform another operation?\nPlease type [Y] to confirm or [N] to decline: ").upper()
            print()

        if repeat == "Y":
            print("Returning to the main menu...\n")

        else:
            done = "OK"

    else:
        print("Returning to the main menu...")


print("\nWellcome to my currency converter!")
while done == "NO":
    select_menu()
    from_currency_code = input_1()
    from_currency_value = currencies_data[from_currency_code]["value"]
    from_currency_name = currencies_data[from_currency_code]["name"]
    
    print(f'You selected: {from_currency_name} [{from_currency_code}]')
    
    to_currency_code = input_2()
    to_currency_value = currencies_data[to_currency_code]["value"]
    to_currency_name = currencies_data[to_currency_code]["name"]
    
    print(f'You selected: {to_currency_name} [{to_currency_code}]')
    
    amount = input_3(from_currency_code)
    converted_amount = convert(amount, from_currency_value, to_currency_value)
    commission = income(converted_amount, slice)
    withdraw_amount = round(converted_amount,2) - round(commission,2)
    
    confirm(amount, from_currency_name, converted_amount, to_currency_name, commission, withdraw_amount)












