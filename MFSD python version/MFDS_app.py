from unicodedata import name

from entities.Fuel import Fuel
from entities.FuelAttendant import FuelAttendant

while True:
    main_menu = """
    Welcome to MFDS Fluids App!
    
    1. Register as a fuel attendant
    0. Exit
    """
    print(main_menu)
    user_input = input("Make a selection: ")
    match user_input:
        case "1":
            while True:
                first_name = input("What is your first name? ")
                second_name = input("What is your second name? ")
                fuel_attendant = FuelAttendant(first_name, second_name)
                print("Successfully registered!")
                fuel_attendant_menu = f"""
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
                print(fuel_attendant_menu)
                select = input("make a selection: ")
                match select:
                    case "1":
                        fuel_name = input("What is the fuel name? ")
                        fuel_price = input("What is the fuel price per liter? ")
                        fuel_amount = input("What is the fuel total amount? ")
                        new_fuel = Fuel(fuel_name, fuel_price, fuel_amount)
                        print("Successfully added!")
                    case "2":
                        for fuel in fuel_attendant.get_available_fuels():
                            print(fuel)

                    case "0": break
                    case _:
                        print("Invalid selection!")

        case "0": break
        case _: print("Invalid input")

