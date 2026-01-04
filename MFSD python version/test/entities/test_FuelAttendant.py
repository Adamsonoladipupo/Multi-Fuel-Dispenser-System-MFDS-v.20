from unittest import TestCase

from entities.Fuel import Fuel
from entities.FuelAttendant import FuelAttendant


class TestFuelAttendant(TestCase):
    def test_sell_2000_Naira_fuel_for_a_customer(self):
        fuel_attendant = FuelAttendant("Ola", "Marc")
        fuel = Fuel("Gasoline", 1000, 50)
        fuel_attendant.add_fuel(fuel)
        self.assertFalse(fuel_attendant.is_empty())
        fuel_attendant.dispense_fuel_by_price("gasoline", 2000)
        self.assertEqual(48, fuel.get_quantity())

        for record in fuel_attendant.get_records():
            print(record)

        for fuel in fuel_attendant.get_available_fuels().values():
            print(fuel)

