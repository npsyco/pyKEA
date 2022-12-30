# In Python, a decorator is a design pattern that allows you to 
# modify the functionality of a function or class without changing 
# its code. Decorators are implemented as callable objects 
# (functions, classes, or methods) that take another function 
# or class and extend the behavior of the latter function or 
# class, without explicitly modifying its code.

# Here is an example of how to use a decorator to add a new 
# feature to a function:

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before calling the decorated function")
        result = func(*args, **kwargs)
        print("After calling the decorated function")
        return result
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("John")

# The output of this code would be:

# Before calling the decorated function
# Hello, John!
# After calling the decorated function

# In this example, the my_decorator function is a decorator that 
# takes a function as an argument (the greet function) and returns 
# a wrapper function that extends the behavior of the original 
# function. The @my_decorator syntax is a short way of saying 
# greet = my_decorator(greet), which assigns the wrapper function 
# returned by my_decorator to the greet variable.

# Decorators can be used to add or modify the behavior of functions 
# or classes in a consistent and reusable way. They are often used 
# to implement cross-cutting concerns, such as logging, caching, 
# and authentication, which are not specific to the business logic 
# of a function or class but are necessary for the overall 
# functioning of the application.

