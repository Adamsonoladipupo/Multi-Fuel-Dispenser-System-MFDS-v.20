class Fuel:
    def __init__(self, name, price_per_liter, quantity):
        self.name = name
        self.price_per_liter = price_per_liter
        self.quantity = quantity

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def set_price_per_liter(self, price):
        self.price_per_liter = price

    def get_price_per_liter(self):
        return self.price_per_liter

    def set_quantity(self, new_quantity):
        self.quantity = new_quantity

    def get_quantity(self):
        return self.quantity



