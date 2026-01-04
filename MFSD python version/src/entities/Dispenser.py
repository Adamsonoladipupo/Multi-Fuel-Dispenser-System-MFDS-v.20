from entities.Fuel import Fuel

from exceptions.FuelDuplicateException import FuelDuplicateException
from exceptions.FuelQuantityIsNotLowException import FuelQuantityIsNotLowException
from exceptions.NonExistingFuelException import NonExistingFuelException


class Dispenser:
    def __init__(self):
        self.__fuel_store = {}

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

    def validate_fuel_existence(self, fuel: Fuel):
        if fuel.name not in self.__fuel_store.keys():
            raise NonExistingFuelException ("Fuel does not exist")

    def validate_fuel_existence_by_name(self, fuel_name):
        if fuel_name not in self.__fuel_store.keys():
            raise NonExistingFuelException("Fuel does not exist")


    def restock_fuel(self, fuel_name, ):
        if fuel_name in self.__fuel_store:
            fuel = self.get_fuel_by_name(fuel_name)
            if fuel.get_price_per_liter() < 50:
                fuel.set_quantity(50)
            elif fuel.get_price_per_liter() == 50:
                raise FuelQuantityIsNotLowException("Fuel quantity is not low")
        else:
            raise NonExistingFuelException ("Fuel does not exist")

    def validate_fuel_non_existence(self, fuel: Fuel):
        if fuel.name in self.__fuel_store:
            raise FuelDuplicateException ("Fuel is already exists")

    def validate_fuel_non_existence_by_name(self, fuel_name):
        if fuel_name not in self.__fuel_store.keys():
            raise FuelDuplicateException ("Fuel is already exists")



