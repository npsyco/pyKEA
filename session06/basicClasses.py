class Dog:
    # Class Attributes
    species = "canines"

    # Methods like __init__ and __str__ are called dunder methods.
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

    # Instance method
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    


    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"