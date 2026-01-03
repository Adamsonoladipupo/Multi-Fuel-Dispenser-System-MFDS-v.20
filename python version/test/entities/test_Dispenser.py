from unittest import TestCase

from entities.Dispenser import Dispenser
from entities.Fuel import Fuel


class TestDispenser(TestCase):
    def test_if_dispenser_isEmpty(self):
        dispenser = Dispenser
        #self.assertTrue(dispenser.is_empty())
        fuel = Fuel("kerosene", 500, 50)
        print(fuel)

