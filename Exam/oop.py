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

# Set the person's age
person.age = 31
