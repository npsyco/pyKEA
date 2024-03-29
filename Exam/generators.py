import os
from colors import bcolors
import itertools
from time import sleep

# In Python, a generator is a special type of function that allows 
# you to iterate over a sequence of values, one at a time, instead 
# of returning the entire sequence all at once. Generators are used 
# to create iterators, but with a different approach. When an ordinary 
# function is called, it executes a block of code and returns a single 
# value. A generator, on the other hand, is a function that returns 
# an iterator object, which allows you to execute the function's 
# code block one step at a time, and return a value only when the 
# generator is "yielded."

print(bcolors.OKBLUE + "To create a generator in Python, you use the yield keyword ")
print("instead of return. When the generator function is called, it ")
print("does not execute the code block immediately. Instead, it returns ")
print("a generator object that can be iterated over to execute the code ")
print("block one step at a time." + bcolors.ENDC)
input("Next?")
print(bcolors.OKCYAN + "Here is an example of a simple generator function that generates ")
print("a sequence of numbers:" + bcolors.ENDC)

def generator_example():
  for i in range(5):
    yield i * i

for i in generator_example():
  print(i)

# This code will output the numbers 0 through 4.

# Generators are often used to generate large sequences of data 
# that would be impractical to store in memory all at once. They 
# allow you to iterate over the sequence one value at a time, 
# which can be more efficient and memory-friendly than storing 
# the entire sequence in memory at once.

# Note that the generator function only generates values when they 
# are requested, which makes generators an efficient way to generate 
# sequences of data. Additionally, once a generator has generated
# all of its values, it cannot be reused, so you have to create a 
# new generator if you want to iterate over the sequence again.

# Generators are also useful for generating infinite sequences. 
# For example, the following generator function generates an infinite 
# sequence of numbers:
input("Next?")
os.system("cls")
print("Infinite sequence:")
def infinite_sequence():
    i = 0
    while True:
        yield i
        i += 1

print(bcolors.OKCYAN + "This generator can be used to generate a specific number of values by ")
print("using the itertools.islice function:" + bcolors.ENDC)

input("Next?")
for num in itertools.islice(infinite_sequence(), 50):
    print(num)

input(bcolors.WARNING + "DANGER: Overflow could result from this. Continue?" + bcolors.ENDC)

for i in infinite_sequence():
   print(i)
   sleep(0.2)