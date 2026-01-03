from unittest import TestCase

from entities.Fuel import Fuel


class TestFuel(TestCase):
    def test_name(self):
        fuel = Fuel("Kerosene", 500, 50)
        self.assertEqual(fuel.name, "Kerosene")

    def test_price(self):
        fuel = Fuel("Kerosene", 500, 50)
        self.assertEqual(fuel.get_price_per_liter(), 500)

    def test_fuel_qnatity(self):
        fuel = Fuel("Kerosene", 500, 50)
        self.assertEqual(fuel.get_quantity(), 50)
        print(fuel)


