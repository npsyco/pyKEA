# In Python, a generator is a special type of function that allows 
# you to iterate over a sequence of values, one at a time, instead 
# of returning the entire sequence all at once. Generators are used 
# to create iterators, but with a different approach. When an ordinary 
# function is called, it executes a block of code and returns a single 
# value. A generator, on the other hand, is a function that returns 
# an iterator object, which allows you to execute the function's 
# code block one step at a time, and return a value only when the 
# generator is "yielded."

# To create a generator in Python, you use the yield keyword 
# instead of return. When the generator function is called, it 
# does not execute the code block immediately. Instead, it returns 
# a generator object that can be iterated over to execute the code 
# block one step at a time.

# Here is an example of a simple generator function that generates 
# a sequence of numbers:

def generator_example():
  for i in range(5):
    yield i

for i in generator_example():
  print(i)

# This code will output the numbers 0 through 4.

# Generators are often used to generate large sequences of data 
# that would be impractical to store in memory all at once. They 
# allow you to iterate over the sequence one value at a time, 
# which can be more efficient and memory-friendly than storing 
# the entire sequence in memory at once.