from coffee import Coffee
from order import Order

class Customer:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if type(value) == str and 1 <= len(value) <= 15:
            self._name = value
        else: 
            print("Name must have a value between 1 and 15 characters")
    
    def orders(self):
        return [order for order in Order.all if order.customer == self]

    def coffees(self):
        return list(set(order.coffee for order in self.orders))
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
c1 = Customer("Josh")

print(c1.name)