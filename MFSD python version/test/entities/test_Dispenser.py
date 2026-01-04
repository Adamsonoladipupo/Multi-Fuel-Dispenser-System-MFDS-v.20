from unittest import TestCase

from entities.Dispenser import Dispenser
from entities.Fuel import Fuel
from exceptions.FuelDuplicateException import FuelDuplicateException
from exceptions.NonExistingFuelException import NonExistingFuelException


class TestDispenser(TestCase):
    def test_is_empty(self):
        dispenser = Dispenser()
        self.assertTrue(dispenser.is_empty())

    def test_add_fuel(self):
        dispenser = Dispenser()
        fuel = Fuel("Kerosene", 1000, 50)
        dispenser.add_fuel(fuel)
        self.assertFalse(dispenser.is_empty())

    def test_add_an_already_existing_fuel(self):
        dispenser = Dispenser()
        fuel = Fuel("Kerosene", 1000, 50)
        dispenser.add_fuel(fuel)
        self.assertRaises(FuelDuplicateException, dispenser.add_fuel, fuel)

    def test_update_existing_fuel_price(self):
        dispenser = Dispenser()
        fuel = Fuel("Gasoline", 1000, 50)
        dispenser.add_fuel(fuel)
        self.assertFalse(dispenser.is_empty())
        dispenser.update_fuel_price("gasoline", 1200)
        self.assertEqual(1200, fuel.get_price_per_liter())


    def test_update_non_existing_fuel_price(self):
        dispenser = Dispenser()
        fuel = Fuel("Kerosene", 1000, 50)
        dispenser.add_fuel(fuel)
        self.assertFalse(dispenser.is_empty())
        # dispenser.update_fuel_price("Petrol", 1200)
        self.assertRaises(NonExistingFuelException, dispenser.update_fuel_price, "Petrol", 1200)

