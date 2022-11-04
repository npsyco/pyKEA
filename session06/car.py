class Car:
    def __init__(self, color:str, mileage:int ):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f" The {self.color} car has driven {self.mileage} miles."


#if __name__ == "__main__":
 #   blue = Car("Blue", 2000)
  #  print(blue)