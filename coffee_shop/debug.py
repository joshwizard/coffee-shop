from customer import Customer
from coffee import Coffee
from order import Order

# Create customers
customer1 = Customer("Josh")
customer2 = Customer("Sarah")

# Create coffees
coffee1 = Coffee("Black_coffee")
coffee2 = Coffee("White_coffee")

# Create orders
order1 = customer1.create_order(coffee1, 3.5)
order2 = customer2.create_order(coffee1, 4.0)
order3 = customer1.create_order(coffee2, 5.5)
order4 = customer2.create_order(coffee1, 3.0)

# Test relationships
print("Customer1 orders:", len(customer1.orders()))
print("Customer1 coffees:", [c.name for c in customer1.coffees()])
print("Coffee1 orders:", coffee1.num_orders())
print("Coffee1 customers:", [c.name for c in coffee1.customers()])
print("Coffee1 average price:", coffee1.average_price())

# Test most aficionado
aficionado = Customer.most_aficionado(coffee1)
print("Most aficionado for Black_coffee:", aficionado.name if aficionado else None)

print("All tests completed successfully!")