import os
from colors import bcolors

print(bcolors.OKBLUE + "In Python, a decorator is a design pattern that allows you to ")
print("modify the functionality of a function or class without changing ")
print("its code. " + bcolors.ENDC)
input("Next?")
print(bcolors.OKGREEN + "Decorators are implemented as callable objects ")
print("(functions, classes, or methods) that take another function ")
print("or class and extend the behavior of the latter function or ")
print("class, without explicitly modifying its code." + bcolors.ENDC)
input("Next?")
os.system("cls")
print(bcolors.OKCYAN + "Here is an example of how to use a decorator to add a new ")
print("feature to a function:" + bcolors.ENDC)
input("Next?")
def my_decorator(func):
    def wrapper(*arguments): # the wrapper returned is assigned to the 'greet' variable
        print(bcolors.WARNING + "Before calling the decorated function" + bcolors.ENDC)
        input("Next?")
        result = func(*arguments)
        print(bcolors.OKGREEN + "After calling the decorated function" + bcolors.ENDC)
        input("Next?")
        return result
    return wrapper

@my_decorator
def greet(name): # name is the greet variable
    print(f"Hello, {name}!")

user_input = input("Enter your name: ")
greet(user_input)

# The output of this code would be:

# Before calling the decorated function
# Hello, <user_input>!
# After calling the decorated function

# In this example, the 'my_decorator' function is a decorator that 
# takes a function as an argument (the greet function) and returns 
# a wrapper function that extends the behavior of the original 
# function. The '@my_decorator' syntax is a short way of saying 
# greet = my_decorator(greet), which assigns the wrapper function 
# returned by 'my_decorator' to the 'greet' variable.

# By using the unpacking operator (*), we can parse in any object.
# The **kwargs unpacking operator is used on dictonaries.

# Decorators can be used to add or modify the behavior of functions 
# or classes in a consistent and reusable way. They are often used 
# to implement cross-cutting concerns, such as logging, caching, 
# and authentication, which are not specific to the business logic 
# of a function or class but are necessary for the overall 
# functioning of the application.

# To decorate a class in Python, you can define a decorator 
# function that takes a class as an argument and returns a 
# modified version of the class. The decorator function can 
# modify the attributes and methods of the class in any way 
# that you desire.

print(bcolors.OKCYAN + "Here is an example of a decorator that adds a new attribute ")
print("and a new method to a class:" + bcolors.ENDC)
input("Next?")
def class_decorator(cls):
    cls.new_attribute = bcolors.OKBLUE + "This is a new attribute added by the decorator" + bcolors.ENDC
    def new_method(self):
        print(bcolors.OKGREEN + "This is a new method added by the decorator" + bcolors.ENDC)
    cls.new_method = new_method
    return cls

@class_decorator
class MyClass:
    def __init__(self, value):
        self.value = value

obj = MyClass("value")
print("The new attribute:")
print(obj.new_attribute)
print("Now the new method:")
obj.new_method()

# Output: 
# This is a new attribute added by the decorator
# This is a new method added by the decorator

# To apply the decorator to a class, you can use the @ symbol 
# followed by the name of the decorator, like this:

@class_decorator
class MyClass:
    pass
    # ...

# This is equivalent to writing:

# class MyClass:
    # ...
# MyClass = class_decorator(MyClass)

# In Python, decorating a class means modifying the class in some 
# way by wrapping it with another function or class. The decorator 
# function or class takes the original class as an argument and 
# returns a modified version of the class. This is similar to 
# the way that decorators work for functions.

# In Java, inheritance is a mechanism for creating a new class 
# that is a modified version of an existing class. The new class, 
# called the subclass, inherits the attributes and methods of the 
# existing class, called the superclass. The subclass can add or 
# override the attributes and methods of the superclass to create 
# a specialized version of the superclass.

# There are some similarities and differences between decorating a 
# class in Python and inheriting in Java:

# Similarities:

# Both decorating a class in Python and inheriting in Java allow 
# you to create a modified version of an existing class.
# In both cases, you can add or modify the attributes and methods 
# of the original class to create a specialized version of the class.

# Differences:

# Syntax: Decorating a class in Python uses the @ symbol followed 
# by the name of the decorator, while inheritance in Java uses 
# the extends keyword.

# Scope: Decorating a class in Python applies the modifications 
# to a single instance of the class, while inheritance in Java 
# applies the modifications to all instances of the subclass.

# Multiple inheritance: Python allows a class to be decorated by 
# multiple decorators, but Java does not allow a class to inherit 
# from multiple superclasses. Instead, Java provides the implements 
# keyword for implementing multiple interfaces, which define a set 
# of methods that a class must implement.