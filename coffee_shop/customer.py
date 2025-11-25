from coffee import Coffee

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

c1 = Customer("Josh")

print(c1.name)