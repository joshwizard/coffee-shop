import pytest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from customer import Customer
from coffee import Coffee
from order import Order

class TestCoffee:
    def setup_method(self):
        Order.all = []

    def test_coffee_init(self):
        coffee = Coffee("Black_coffee")
        assert coffee.name == "Black_coffee"

    def test_coffee_name_validation(self):
        with pytest.raises(ValueError):
            Coffee("AB")
        with pytest.raises(ValueError):
            Coffee(123)

    def test_coffee_orders(self):
        customer = Customer("Josh")
        coffee = Coffee("Black_coffee")
        order = Order(customer, coffee, 3.5)
        assert len(coffee.orders()) == 1
        assert coffee.orders()[0] == order

    def test_coffee_customers(self):
        customer1 = Customer("Josh")
        customer2 = Customer("Sarah")
        coffee = Coffee("Black_coffee")
        Order(customer1, coffee, 3.5)
        Order(customer2, coffee, 4.0)
        customers = coffee.customers()
        assert len(customers) == 2
        assert customer1 in customers
        assert customer2 in customers

    def test_num_orders(self):
        customer = Customer("Josh")
        coffee = Coffee("Black_coffee")
        Order(customer, coffee, 3.5)
        Order(customer, coffee, 4.0)
        assert coffee.num_orders() == 2

    def test_average_price(self):
        customer = Customer("Josh")
        coffee = Coffee("Black_coffee")
        Order(customer, coffee, 3.0)
        Order(customer, coffee, 5.0)
        assert coffee.average_price() == 4.0