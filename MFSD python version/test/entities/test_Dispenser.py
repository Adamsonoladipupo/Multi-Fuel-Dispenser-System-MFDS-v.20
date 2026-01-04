from unittest import TestCase

from entities.Dispenser import Dispenser
from entities.Fuel import Fuel
from exceptions.FuelDuplicateException import FuelDuplicateException
from exceptions.FuelQuantityIsNotLowException import FuelQuantityIsNotLowException
from exceptions.InvalidHighPriceException import InvalidHighPriceException
from exceptions.InvalidLowPriceException import InvalidLowPriceException
from exceptions.InvalidNegativeLiterException import InvalidNegativeLiterException
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

    def test_restock_an_existing_fuel_price(self):
        dispenser = Dispenser()
        fuel = Fuel("Gasoline", 1000, 50)
        dispenser.add_fuel(fuel)
        dispenser.restock_fuel("gasoline", 10)
        self.assertEqual(60, fuel.get_quantity())

    def test_restock_non_existing_fuel_price(self):
        dispenser = Dispenser()
        fuel = Fuel("Gasoline", 1000, 50)
        self.assertRaises(NonExistingFuelException, dispenser.restock_fuel, "gasoline", 10)

    def test_dispense_fuel_by_price(self):
        dispenser = Dispenser()
        fuel = Fuel("Gasoline", 100, 50)
        dispenser.add_fuel(fuel)
        self.assertFalse(dispenser.is_empty())
        dispenser.dispense_fuel_by_price("gasoline", 100)
        self.assertEqual(49, fuel.get_quantity())

    def test_dispense_fuel_by_price_below_the_fuel_1_liter_price(self):
        dispenser = Dispenser()
        fuel = Fuel("Gasoline", 100, 50)
        dispenser.add_fuel(fuel)
        self.assertFalse(dispenser.is_empty())
        self.assertRaises(InvalidLowPriceException, dispenser.dispense_fuel_by_price, "gasoline", 90)
        self.assertEqual(50, fuel.get_quantity())

    def test_dispense_fuel_by_price_above_the_fuel_50_liters_price(self):
        dispenser = Dispenser()
        fuel = Fuel("Gasoline", 100, 500)
        dispenser.add_fuel(fuel)
        self.assertFalse(dispenser.is_empty())
        self.assertRaises(InvalidHighPriceException, dispenser.dispense_fuel_by_price, "gasoline", 5001)
        self.assertEqual(500, fuel.get_quantity())

    def test_dispense_fuel_by_price_below_the_fuel_total_quantity(self):
        dispenser = Dispenser()
        fuel = Fuel("Gasoline", 100, 2)
        dispenser.add_fuel(fuel)
        self.assertFalse(dispenser.is_empty())
        self.assertRaises(InvalidLowPriceException, dispenser.dispense_fuel_by_price, "gasoline", 0)
        self.assertEqual(2, fuel.get_quantity())

    def test_dispense_fuel_by_price_above_the_fuel_total_quantity(self):
        dispenser = Dispenser()
        fuel = Fuel("Gasoline", 100, 1)
        dispenser.add_fuel(fuel)
        self.assertFalse(dispenser.is_empty())
        self.assertRaises(FuelQuantityIsNotLowException, dispenser.dispense_fuel_by_price, "gasoline", 1200)
        self.assertEqual(1, fuel.get_quantity())

    def test_dispense_fuel_by_liters(self):
        dispenser = Dispenser()
        fuel = Fuel("Gasoline", 100, 50)
        dispenser.add_fuel(fuel)
        self.assertFalse(dispenser.is_empty())
        dispenser.dispense_fuel_by_liters("gasoline", 5)
        self.assertEqual(45, fuel.get_quantity())

    def test_dispense_fuel_by_liters_above_the_fuel_total_quantity(self):
        dispenser = Dispenser()
        fuel = Fuel("Gasoline", 100, 5)
        dispenser.add_fuel(fuel)
        self.assertFalse(dispenser.is_empty())
        self.assertRaises(FuelQuantityIsNotLowException, dispenser.dispense_fuel_by_liters, "gasoline", 5.5)
        self.assertEqual(5, fuel.get_quantity())

    def test_dispense_fuel_by_liters_below_the_fuel_total_quantity(self):
        dispenser = Dispenser()
        fuel = Fuel("Gasoline", 100, 5)
        dispenser.add_fuel(fuel)
        self.assertFalse(dispenser.is_empty())
        self.assertRaises(InvalidNegativeLiterException, dispenser.dispense_fuel_by_liters, "gasoline", -10)
        self.assertEqual(5, fuel.get_quantity())

    def test_dispense_fuel_by_liters_below_1_liter(self):
        dispenser = Dispenser()
        fuel = Fuel("Gasoline", 100, 5)
        dispenser.add_fuel(fuel)
        self.assertFalse(dispenser.is_empty())
        self.assertRaises(InvalidLowPriceException, dispenser.dispense_fuel_by_liters, "gasoline", 0.7)
        self.assertEqual(5, fuel.get_quantity())