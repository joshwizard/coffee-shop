class Coffee:
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance (value, str):
            raise TypeError("Text must be of string type")
        
        if len(value) < 3:
            print("Coffee name must have at least 3 characters")
        
        self._name = value
