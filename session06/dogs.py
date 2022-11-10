class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} barks: {sound}"

class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    def speak(self, sound="bull"):
        return super().speak(sound)

if __name__ == "__main__":
    miles = JackRussellTerrier("Miles", 2000)
    buddy = Dachshund("Buddy", 9)
    jack = Bulldog("Jack", 3)
    jim = Bulldog("Jim", 1)
    print(miles, buddy, jack, jim)
    print(type(miles))
    print(isinstance(miles, Dog))
    print(isinstance(miles, Bulldog))
    print(miles.speak())
    print(jim.speak("wiif"))
    print(jack.speak())