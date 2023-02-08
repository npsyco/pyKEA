# Getters and setters, also known as accessors and mutators, 
# are methods that are used to get or set the value of an 
# object's data attributes. These methods are used to encapsulate 
# the internal representation of an object, which means that they 
# allow the programmer to control how the object's data is accessed 
# and modified.

# Here is an example of a simple Python class that has a getter 
# and setter method:

class Person:
  def __init__(self, name, age):
    self._name = name
    self._age = age
    
  # Getter method
  def get_name(self):
    return self._name
  
  # Setter method
  def set_name(self, name):
    self._name = name
    
  # Getter method
  def get_age(self):
    return self._age
  
  # Setter method
  def set_age(self, age):
    self._age = age

# In this example, the Person class has two data attributes: 
# name and age. The getter and setter methods for each attribute 
# allow the programmer to access and modify the values of these 
# attributes in a controlled way.

# To use the getter and setter methods, you would create an instance 
# of the Person class and then call the appropriate method:

# Create an instance of the Person class
person = Person("John", 30)

# Get the person's name
name = person.get_name()  # Returns "John"

# Set the person's age
person.set_age(31)

# In Python, it is also possible to use property decorators to 
# define getters and setters. Here is the same example as above, 
# but using property decorators:

class Person:
  def __init__(self, name, age):
    self._name = name
    self._age = age
    
  # Getter method
  @property
  def name(self):
    return self._name
  
  # Setter method
  @name.setter
  def name(self, name):
    self._name = name
    
  # Getter method
  @property
  def age(self):
    return self._age
  
  # Setter method
  @age.setter
  def age(self, age):
    self._age = age

# Using property decorators allows you to access and modify the 
# data attributes of the Person class using dot notation, just 
# like any other attribute:

# Create an instance of the Person class
person = Person("John", 30)

# Get the person's name
name = person.name  # Returns "John"
age = person.age
print(name, age)
# Set the person's age
person.age = 31
age = person.age
print(age)
# Inheritance is a way to create a new class that is a 
# modified version of an existing class. The new class 
# is called the subclass and the existing class is the 
# superclass. The subclass inherits attributes and 
# behaviors from the superclass and can also have additional 
# attributes and behaviors of its own.

# Single inheritance is when a subclass inherits from a single 
# superclass. For example:

class Animal:
  def __init__(self, name, species):
    self.name = name
    self.species = species
    
  def make_sound(self):
    print("Some generic animal sound")
    
class Dog(Animal):
  def __init__(self, name, breed):
    super().__init__(name, species="Dog")
    self.breed = breed
    
  def make_sound(self):
    print("Bark")

# In this example, the 'Dog' class is a subclass of the 'Animal' 
# class and it inherits the name and species attributes and 
# the make_sound method from the 'Animal' class. The 'Dog' class 
# also has an additional attribute, 'breed', and it has its own 
# implementation of the 'make_sound' method.

# Making a dog using the 'Dog' class:

dog = Dog("Vovse", "Border Collie")
print(dog.name) # Vovse
print(dog.breed) # Border Collie
dog.make_sound() # Bark

# Multiple inheritance is when a subclass inherits from multiple 
# superclasses. For example:

class Animal:
  def __init__(self, name, species):
    self.name = name
    self.species = species
    
  def make_sound(self):
    print("Some generic animal sound")
    
class Pet:
  def __init__(self, name, owner):
    self.name = name
    self.owner = owner
    
  def set_owner(self, owner):
    self.owner = owner
    
class Dog(Animal, Pet):
  def __init__(self, name, breed, owner):
    Animal.__init__(self, name, species="Dog")
    Pet.__init__(self, name, owner)
    self.breed = breed
    
  def make_sound(self):
    print("Vov")

# In this example, the Dog class inherits from both 
# the Animal and Pet classes and it has access to all 
# of the attributes and methods from both of these classes.

# Creating a Dog/Pet using multiple inheritance:

pet = Dog("Fido", "Golden Retriever", "Christian")

print(pet.name) # Fido
print(pet.breed) # Golden Retriever
print(pet.owner) # Christian
pet.make_sound() # Vov

# Changing the owner:

pet.set_owner("Claus")
print(pet.owner) # Claus