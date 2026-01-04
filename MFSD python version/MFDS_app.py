from unicodedata import name

from entities.Fuel import Fuel
from entities.FuelAttendant import FuelAttendant

def main_menu():
    menu = """
    Welcome to MFDS Fluids App!
    
    Proceed to:
    Register as a fuel attendant 
    
    """
    print(menu)

def attendant_menu():
    menu = f"""
    Welcome {first_name}
    1. Add a new fuel to dispenser
    2. Get available fuels
    3. Update fuel price
    4. Restock fuel
    5. Sell fuel by price
    6. Sell fuel by liters
    7. Check all transactions

    0. Back to main menu

    """
    print(menu)

main_menu()
first_name = input("What is your first name? ")
second_name = input("What is your second name? ")
fuel_attendant = FuelAttendant(first_name, second_name)
print("Successfully registered!")
while True:
    attendant_menu()
    select = input("make a selection: ")
    match select:
        case "1":
            fuel_name = input("What is the fuel name? ").lower()
            fuel_price = int(input("What is the fuel price per liter? "))
            fuel_amount = int(input("What is the fuel total amount? "))
            new_fuel = Fuel(fuel_name, fuel_price, fuel_amount)
            fuel_attendant.add_fuel(new_fuel)
            print("Successfully added!")
        case "2":
            if not fuel_attendant.get_available_fuels():
                print("No available fuel found!")
            else:
                for fuel in fuel_attendant.get_available_fuels().values():
                    print("-------------------")
                    print(fuel)
                    print("-------------------")
        case "3":
             fuel_name = input("What is the fuel name? ").lower()
             fuel_price = int(input("What is the fuel price per liter? "))
             fuel_attendant.update_fuel_price(fuel_name, fuel_price)
             print("Successfully updated!")
        case "4":
            fuel_name = input("What is the fuel name? ").lower()
            fuel_quantity = int(input("What is the fuel quantity? "))
            fuel_attendant.restock_fuel(fuel_name, fuel_quantity)
            print("Successfully restored!")
        case "5":
            fuel_name = input("What is the fuel name? ").lower()
            cost = int(input("How much fuel are you buying? "))
            fuel_attendant.dispense_fuel_by_price(fuel_name, cost)
            print("Successfully dispensed!")
        case "6":
            fuel_name = input("What is the fuel name? ").lower()
            amount = int(input("What is the fuel quantity? "))
            fuel_attendant.dispense_fuel_by_liters(fuel_name, amount)
            print("Successfully dispensed!")
        case "7":
            if not fuel_attendant.get_records():
                print("No records found")
            else:
                for record in fuel_attendant.get_records():
                    print(record)
        case "0":
            break
        case _:
            print("Invalid selection!")
