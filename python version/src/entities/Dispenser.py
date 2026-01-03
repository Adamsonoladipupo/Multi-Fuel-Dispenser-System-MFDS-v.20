class Dispenser:
    count = 0

    def __init__(self, fuels):
        self.fuels = fuels

    def is_empty(self):
        return self.count == 0

    def add_fuel(self, new_fuel):
        self.fuels.append(new_fuel)
        self.count += 1


    def get_fuel(self, fuel_name):
        if fuel_name in self.fuels:
            return self.fuels[fuel_name]
        else:
            return None

    def __str__(self):
        for fuel in self.fuels:
            return f'name: {fuel.name}, price: {fuel.get_price()}, quantity: {fuel.get_quantity()}'








