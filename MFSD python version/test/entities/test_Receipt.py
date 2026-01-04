from unittest import TestCase

from entities.Receipt import Receipt

import datetime

class TestReceipt(TestCase):
    def test_receipt_to_string(self):
        date = datetime.date.today()
        time = datetime.datetime.now().time()

        receipt = Receipt("Shark Fuel", "Gas", 2000,20, date, time)
        receipt2 = Receipt("100%-Eff Fluid", "Petrol", 5000, 60, date, time)
        print(receipt)
        print(receipt2)

