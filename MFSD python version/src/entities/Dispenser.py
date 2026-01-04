from entities.Fuel import Fuel
from entities.Receipt import Receipt
import datetime

from exceptions.FuelDuplicateException import FuelDuplicateException
from exceptions.FuelQuantityIsNotLowException import FuelQuantityIsNotLowException
from exceptions.InvalidLowPriceException import InvalidLowPriceException
from exceptions.InvalidHighPriceException import InvalidHighPriceException
from exceptions.InvalidNegativeLiterException import InvalidNegativeLiterException
from exceptions.NonExistingFuelException import NonExistingFuelException


class Dispenser:
    def __init__(self):
        self.name = "MFDS Fluids"
        self.__fuel_store = {}
        self.__records = []

    def change_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_records(self):
        return self.__records

    def add_record(self, record):
        self.__records.append(record)

    def add_fuel (self, fuel: Fuel):
        self.validate_fuel_non_existence(fuel)
        self.__fuel_store[fuel.name] = fuel

    def is_empty(self):
        return len(self.__fuel_store) == 0

    def get_available_fuels(self):
        return self.__fuel_store

    def number_of_fuels(self):
        return len(self.__fuel_store)

    def get_fuel_by_name(self, name):
        return self.__fuel_store[name]

    def update_fuel_price(self, fuel_name, price):
        self.validate_fuel_existence_by_name(fuel_name)
        self.get_fuel_by_name(fuel_name).set_price_per_liter(price)

    def restock_fuel(self, fuel_name, quantity):
        self.validate_fuel_existence_by_name(fuel_name)
        self.__fuel_store[fuel_name].quantity += quantity

    def dispense_fuel_by_price(self, fuel_name, price):
        self.validate_fuel_existence_by_name(fuel_name)
        self.validate_input_attendant_price(fuel_name, price)
        liter = price / self.__fuel_store[fuel_name].price_per_liter
        self.validate_liter_to_be_dispensed(fuel_name, liter)
        self.__fuel_store[fuel_name].quantity -= liter

        date = datetime.date.today()
        time = datetime.datetime.now().time()
        new_receipt = Receipt(self.name, fuel_name, price, liter,date, time)
        self.__records.append(new_receipt)

        return liter

    def dispense_fuel_by_liters(self, fuel_name, liters):
        self.validate_fuel_existence_by_name(fuel_name)
        self.validate_liter_to_be_dispensed(fuel_name, liters)
        price = liters * self.__fuel_store[fuel_name].price_per_liter
        self.validate_input_attendant_price(fuel_name, price)
        self.__fuel_store[fuel_name].quantity -= liters

        date = datetime.date.today()
        time = datetime.datetime.now().time()
        new_receipt = Receipt(self.name, fuel_name, price, liters, date, time)
        self.__records.append(new_receipt)

        return price


    def validate_fuel_existence(self, fuel: Fuel):
        if fuel.name not in self.__fuel_store.keys():
            raise NonExistingFuelException ("Fuel does not exist")

    def validate_fuel_existence_by_name(self, fuel_name):
        if fuel_name not in self.__fuel_store.keys():
            raise NonExistingFuelException("Fuel does not exist")

    def validate_liter_to_be_dispensed(self, fuel_name, quantity):
        if quantity <= 0:
            raise InvalidNegativeLiterException ("Liter is less than 0")
        if quantity > self.__fuel_store[fuel_name].quantity:
            raise FuelQuantityIsNotLowException ("Fuel quantity is lower than input liters")

    def validate_input_attendant_price(self, fuel_name, price):
        if price < self.__fuel_store[fuel_name].price_per_liter:
            raise InvalidLowPriceException ("Fuel price is lower than 1 litre")
        if price > self.__fuel_store[fuel_name].price_per_liter * 50:
            raise InvalidHighPriceException ("Fuel price is higher than 50 litre")

    def validate_fuel_non_existence(self, fuel: Fuel):
        if fuel.name in self.__fuel_store:
            raise FuelDuplicateException ("Fuel is already exists")

    def validate_fuel_non_existence_by_name(self, fuel_name):
        if fuel_name not in self.__fuel_store.keys():
            raise FuelDuplicateException ("Fuel is already exists")



