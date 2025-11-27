class Order:
    all = []
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, value):
        from customer import Customer
        if not isinstance(value, Customer):
            raise ValueError("Customer must be an instance of Customer class")
        self._customer = value
    
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, value):
        from coffee import Coffee
        if not isinstance(value, Coffee):
            raise ValueError("Coffee must be an instance of Coffee class")
        self._coffee = value

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)) or not (1.0 <= value <= 10):
            raise ValueError("Price must be a number between 1.0 and 10.0")
        self._price = float(value)

