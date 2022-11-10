class Car:
    def __init__(self, name, color, mileage):
        self.name = name
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f"The {self.color} car has {self.mileage} miles."