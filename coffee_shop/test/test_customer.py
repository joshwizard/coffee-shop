import pytest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer:
    def setup_method(self):
        Order.all = []

    def test_customer_init(self):
        customer = Customer("Josh")
        assert customer.name == "Josh"

    def test_customer_name_validation(self):
        with pytest.raises(ValueError):
            Customer("")
        with pytest.raises(ValueError):
            Customer("A" * 16)
        with pytest.raises(ValueError):
            Customer(123)

    def test_customer_orders(self):
        customer = Customer("Josh")
        coffee = Coffee("Black_coffee")
        order = customer.create_order(coffee, 3.5)
        assert len(customer.orders()) == 1
        assert customer.orders()[0] == order

    def test_customer_coffees(self):
        customer = Customer("Josh")
        coffee1 = Coffee("Black_coffee")
        coffee2 = Coffee("White_coffee")
        customer.create_order(coffee1, 3.5)
        customer.create_order(coffee2, 4.5)
        coffees = customer.coffees()
        assert len(coffees) == 2
        assert coffee1 in coffees
        assert coffee2 in coffees

    def test_most_aficionado(self):
        customer1 = Customer("Josh")
        customer2 = Customer("Sarah")
        coffee = Coffee("Black_coffee")
        customer1.create_order(coffee, 3.0)
        customer2.create_order(coffee, 5.0)
        assert Customer.most_aficionado(coffee) == customer2