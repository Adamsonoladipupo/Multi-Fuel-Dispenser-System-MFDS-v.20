class Receipt:
    serial_number = 0
    def __init__(self, name, fuel_type, price, quantity, date, time):
        self.name = name
        self.fuel_type = fuel_type
        self.price = price
        self.quantity = quantity
        self.date = date
        self.time = time
        serial_number = Receipt.serial_number + 1


    def __str__(self):
        return f"""
        --------------------------------------
        Serial Number: {self.serial_number}
        ======================================
        Fuel station: {self.name}
        --------------------------------------
        fuel type: {self.fuel_type}
        Price: ₦{self.price}
        Quantity: {self.quantity}ltr
        --------------------------------------
        Date: {self.date}
        Time : {self.time}
        ======================================
            -- Thanks for your patronage --
        --------------------------------------
        """


