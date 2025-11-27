# Test for orders

import pytest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder:
    def setup_method(self):
        Order.all = []

    def test_order_init(self):
        customer = Customer("Josh")
        coffee = Coffee("Black_coffee")
        order = Order(customer, coffee, 3.5)
        assert order.customer == customer
        assert order.coffee == coffee
        assert order.price == 3.5

    def test_order_price_validation(self):
        customer = Customer("Josh")
        coffee = Coffee("Black_coffee")
        with pytest.raises(ValueError):
            Order(customer, coffee, 0.5)
        with pytest.raises(ValueError):
            Order(customer, coffee, 11.0)
        with pytest.raises(ValueError):
            Order(customer, coffee, "invalid")

    def test_order_customer_validation(self):
        coffee = Coffee("Black_-coffee")
        with pytest.raises(ValueError):
            Order("invalid", coffee, 3.5)

    def test_order_coffee_validation(self):
        customer = Customer("Josh")
        with pytest.raises(ValueError):
            Order(customer, "invalid", 3.5)

    def test_order_all_tracking(self):
        customer = Customer("Josh")
        coffee = Coffee("Black_coffee")
        order1 = Order(customer, coffee, 3.5)
        order2 = Order(customer, coffee, 4.0)
        assert len(Order.all) == 2
        assert order1 in Order.all
        assert order2 in Order.all