###### ###### ###### ######- PRIMITIVE DATATYPES -###### ###### ###### ######

import os
from time import sleep
import time

def next_topic(x):
    counter = time.time()
    while (counter + x - counter != 0):
        counter - x/4
        #sleep(x/4)
        print(".", end="")
    # sleep(x/4)
    # print(".", end="")
    # sleep(x/4)
    # print(".", end= "")
    # sleep(x/4)
    # print(".", end="")
    # sleep(x/4)
    # print(".", end="")
    # sleep(x/4)
    os.system("cls")

counter = time.time()
print(counter)


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(bcolors.HEADER + "\n***PRIMITIVES***\n" + bcolors.ENDC)

sleep(1)

a1:str = "a"
print(bcolors.OKCYAN + "This is a typecasted string" + bcolors.ENDC)
print(type(a1))
input()
print(bcolors.OKBLUE + "I chose to use the var:type syntax.\nAlternately we could use the var = type(<VLAUE>).\nIe. a1 = str('a')." + bcolors.ENDC)
input()
a2:float = 0.12
print(bcolors.OKCYAN + "This is a typecasted float" + bcolors.ENDC)
print(type(a2))
input()
print(bcolors.OKBLUE + "You can choose to use the var:type syntax.\nAlternately you can could use the var = type(<VLAUE>).\nIe. a2 = float('0.12')." + bcolors.ENDC)
input()
a3:int = 3
print(bcolors.OKCYAN + "This is a typecasted integer" + bcolors.ENDC)
print(type(a3))
input()
print(bcolors.OKBLUE + "You can choose to use the var:type syntax.\nAlternately you could use the var = type(<VLAUE>).\nIe. a3 = int(3)." + bcolors.ENDC)
input()
a4:bool = True
print(bcolors.OKCYAN + "This is a typecasted boolean" + bcolors.ENDC)
print(type(a4))
input()
print(bcolors.OKBLUE + "You can choose to use the var:type syntax.\nAlternately you could use the var = type(<VLAUE>).\nIe. a4 = bool(<param>).")
print("Here it is reasonable to also mention the eval() function, since the bool() function only evaluates whether a parameter has been passed or not.\n")
print("However, you need to change the var into a string, for eval() to function." + bcolors.ENDC)
print(bcolors.OKCYAN + "Output of eval(True):" + bcolors.ENDC)
a5 = "True"
print(eval(a5))
# list = []
# dict = {}
# tuple = ()
# set = {}

input(bcolors.WARNING + "\nPress 'Enter' to continue to Lists" + bcolors.ENDC)
next_topic(3)

###### ###### ###### ######- LISTS -###### ###### ###### ######

print(bcolors.HEADER + "\n***LISTS***\n" + bcolors.ENDC)

# In Python, a list is an ordered collection of items that 
# can be of any data type, including other lists. Lists are 
# used to store and manipulate data in a structured way.
sleep(1)
print(bcolors.OKCYAN + "Here is an example of how to create a list in Python:" + bcolors.ENDC)

l = [1, 2, 3, 4, 5]
print(l)
# prints [1, 2, 3, 4, 5]
sleep(1.5)
# In this example, we create a list 'l' that contains five integers.

print(bcolors.OKCYAN + "You can access the elements of a list using indexing with list[index]:" + bcolors.ENDC)

print(l[0])  # 1
print(l[1])  # 2
print(l[2])  # 3
print(l[3])  # 4
print(l[4])  # 5
input()
print(bcolors.OKCYAN + "You can also use negative indexing to access the elements of a list from the end with list[-index]:" + bcolors.ENDC)

print(l[-1])  # 5
print(l[-2])  # 4
print(l[-3])  # 3
print(l[-4])  # 2
print(l[-5])  # 1
input()
print(bcolors.OKCYAN + "You can modify the elements of a list by reassigning them with list[index] = <NEW_VALUE>:" + bcolors.ENDC)

l[0] = 10
print(l)  # [10, 2, 3, 4, 5]

l[1] = 20
print(l)  # [10, 20, 3, 4, 5]
input()
print(bcolors.OKCYAN + "You can use slicing to access a range of elements with list[start:stop]:" + bcolors.ENDC)

print(l[2:3]) # [3]
input()
print(bcolors.OKCYAN + "You can modify the amount of jumps during slicing with list[start:stop:jumps]:" + bcolors.ENDC)

print(l[0:5:2]) # [10, 3, 5]
input()
print(bcolors.OKCYAN + "You can reverse the entire list, with the integer defining number of jumps with list[::-jumps]:" + bcolors.ENDC)

print(l[::-2]) # [5, 3, 10]
input()
print(bcolors.OKCYAN + "You can concatenate the list with list1 + list2:" + bcolors.ENDC)

l2 = [6 ,7]
lx = l + l2
print(lx)
input()
print(bcolors.OKCYAN + "Or by using the keyword .extend()" + bcolors.ENDC)
l3 = [8, 9]
l.extend(l3)
print(l)
input()

print(bcolors.OKCYAN + "You can get the length of iterable elements of a list using the len() function:" + bcolors.ENDC)
print(len(l))

print(bcolors.OKCYAN + "You can display the minimum and maximum values in a list using the min() or max() functions:" + bcolors.ENDC)

print(min(l))
print(max(l))


###### ###### ###### ######- DICTIONARIES -###### ###### ###### ######
input(bcolors.WARNING + "\nPress 'Enter' to continue to Dictionaries" + bcolors.ENDC)
next_topic()
print(bcolors.HEADER + "\n***DICTIONARIES***\n" + bcolors.ENDC)

# In Python, a dictionary is a collection of key-value pairs. 
# Dictionaries are used to store and manipulate data that is 
# organized into pairs of keys and values.

print(bcolors.OKCYAN + "Here is an example of how to create a dictionary in Python:" + bcolors.ENDC)

d = {'a': 1, 'b': 2, 'c': 3}
print(d)
# prints {'a': 1, 'b': 2, 'c': 3}

print(bcolors.OKBLUE + "In this example, we create a dictionary 'd' that contains three key-value pairs. The keys are 'a', 'b', and 'c', and the corresponding values are 1, 2, and 3." + bcolors.ENDC)

print(bcolors.OKCYAN + "You can access the values in a dictionary using the keys:" + bcolors.ENDC)

print(d['a'])  # 1
print(d['b'])  # 2
print(d['c'])  # 3

print(bcolors.OKCYAN + "You can also modify the values in a dictionary by reassigning them:" + bcolors.ENDC)

d['a'] = 10
print(d)  # {'a': 10, 'b': 2, 'c': 3}

d['b'] = 20
print(d)  # {'a': 10, 'b': 20, 'c': 3}

d['c'] = 30
print(d)  # {'a': 10, 'b': 20, 'c': 30}

print(bcolors.OKCYAN + "You can add new key-value pairs to a dictionary using the assignment operator:" + bcolors.ENDC)

d['d'] = 40
print(d)  # {'a': 10, 'b': 20, 'c': 30, 'd': 40}

print(bcolors.OKCYAN + "You can delete key-value pairs from a dictionary using the 'del' statement:" + bcolors.ENDC)

del d['a']
print(d)  # {'b': 20, 'c': 30, 'd': 40}


###### ###### ###### ######- TUPLES -###### ###### ###### ######
input(bcolors.WARNING + "\nPress 'Enter' to continue to Tuples" + bcolors.ENDC)
next_topic()
print(bcolors.HEADER + "\n***TUPLES***\n" + bcolors.ENDC)

# In Python, a tuple is an immutable sequence type, while a set 
# is an unordered collection of unique elements. Here are some 
# key differences between tuples and sets:

# Immutability: Tuples are immutable, 
# which means you cannot modify the values they contain. 
# Once you create a tuple, you cannot change the values it contains. 
# In contrast, sets are mutable, which means you can add and remove 
# elements from a set.

# Order: Tuples maintain the order of the elements they contain. 
# This means that the elements in a tuple are stored in a specific 
# order, and this order is preserved when you access the elements 
# of the tuple. In contrast, sets do not maintain any order among 
# their elements.

# Duplicates: Tuples can contain duplicate elements, while sets do 
# not allow duplicate elements. If you try to add a duplicate 
# element to a set, it will be ignored and the set will remain 
# unchanged.

# Indexing: You can access the elements of a tuple using indexing, 
# just like you would with a list. However, sets do not support 
# indexing, as they do not maintain any order among their elements.

# Membership testing: You can use the 'in' operator to test membership 
# in both tuples and sets. However, testing membership in a set 
# is generally faster than testing membership in a tuple, because 
# sets use hash tables for fast membership testing, while tuples 
# do not.

print(bcolors.OKCYAN + "Tuples can contain elements of different types, including other tuples:" + bcolors.ENDC)

t = (1, 'a', 3.14, (5, 6))
print(t)

# prints (1, 'a', 3.14, (5, 6))

print(bcolors.OKCYAN + "You can access the elements of a tuple using indexing, just like you would with a list:" + bcolors.ENDC)

print(bcolors.OKCYAN + "Create a tuple" + bcolors.ENDC)
t = (1, 2, 3, 4, 5)

print(bcolors.OKCYAN + "Access the elements of the tuple using indexing" + bcolors.ENDC)
print(t[0])  # 1
print(t[1])  # 2
print(t[2])  # 3
print(t[3])  # 4
print(t[4])  # 5

print(bcolors.OKCYAN + "You can also use negative indexing to access the elements of the tuple" + bcolors.ENDC)
print(t[-1])  # 5
print(t[-2])  # 4
print(t[-3])  # 3
print(t[-4])  # 2
print(t[-5])  # 1

print(bcolors.OKCYAN + "You can also use slicing to access a range of elements in a tuple:" + bcolors.ENDC)

t = (1, 2, 3, 4, 5)
print(t[1:3])
# prints 2 and 3

print(bcolors.OKGREEN + "One of the main advantages of tuples is that they are immutable, " + bcolors.ENDC)
print(bcolors.OKGREEN + "which means they are less prone to accidental modification and" + bcolors.ENDC) 
print(bcolors.OKGREEN + "can be used as keys in dictionaries and elements in sets. " + bcolors.ENDC)
print(bcolors.OKGREEN + "Tuples are also generally faster and use less memory than lists, " + bcolors.ENDC)
print(bcolors.OKGREEN + "making them a good choice for storing large amounts of data." + bcolors.ENDC)

print(bcolors.OKBLUE + "Here's an example of using a tuple as a key in a dictionary," + bcolors.ENDC) 
print(bcolors.OKBLUE + "as long as the tuple is immutable (i.e., it contains only " + bcolors.ENDC)
print(bcolors.OKBLUE + "immutable elements such as strings, numbers, or other tuples)." + bcolors.ENDC)
next_topic(2)
print(bcolors.OKCYAN + "Create a dictionary with a tuple as the key" + bcolors.ENDC)
d = {(1, 2): 'a', (3, 4): 'b', (5, 6): 'c'}

print(bcolors.OKCYAN + "Access the values in the dictionary using the tuple keys" + bcolors.ENDC)
print(d[(1, 2)])  # 'a'
print(d[(3, 4)])  # 'b'
print(d[(5, 6)])  # 'c'


###### ###### ###### ######- LIST COMPREHENSION -###### ###### ###### ######
input(bcolors.WARNING + "\nPress 'Enter' to continue to List Comprehension" + bcolors.ENDC)
next_topic(1)
print(bcolors.HEADER + "\n***LIST COMPREHENSION***\n" + bcolors.ENDC)

# List comprehension is a concise way to create a list using a 
# single line of code. It is often used to perform a transformation 
# or computation on a sequence of input values and return the 
# resulting list.

print(bcolors.OKCYAN + "Here is an example of a basic list comprehension:" + bcolors.ENDC)

numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers] # x or i
print(squares)
# prints [1, 4, 9, 16, 25]

print(bcolors.OKGREEN + "In this example, the list comprehension [x**2 for x in numbers] " + bcolors.ENDC)
print(bcolors.OKGREEN + "iterates over the 'numbers' list and creates a new list 'squares' " + bcolors.ENDC)
print(bcolors.OKGREEN + "that contains the squares of each number in 'numbers'." + bcolors.ENDC)

print(bcolors.OKBLUE + "List comprehensions can also include an optional conditional " + bcolors.ENDC)
print(bcolors.OKBLUE + "expression, known as a predicate, that filters the input values" + bcolors.ENDC) 
print(bcolors.OKBLUE + "based on a certain condition. For example:" + bcolors.ENDC)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = [x**2 for x in numbers if x % 2 == 0]
print(even_squares)
# prints [4, 16, 36, 64, 100]

print(bcolors.OKGREEN + "In this example, the list comprehension " + bcolors.ENDC)
print(bcolors.OKGREEN + "[x**2 for x in numbers if x % 2 == 0] iterates over the 'numbers' " + bcolors.ENDC)
print(bcolors.OKGREEN + "list and creates a new list 'even_squares' that contains the " + bcolors.ENDC)
print(bcolors.OKGREEN + "squares of only the even numbers in 'numbers'." + bcolors.ENDC)

# In Python, the variable x is often used as a convention for list 
# comprehensions, but you can use any variable name that you like. 
# The variable name x is used to represent each element in the input 
# list or iterable, and is typically used to make the list 
# comprehension more readable.

print(bcolors.OKCYAN + "Here is an example of using the variable 'i' instead of 'x' in a list comprehension:" + bcolors.ENDC)

# Create a list of squares using list comprehension
squares = [i**2 for i in range(1, 11)]
print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# In this example, we use the variable 'i' to represent each element 
# in the input list (which is created using the range() function), 
# and we square each element to create a new list of squares.

# You can use any variable name that you like in a list comprehension, 
# as long as it is a valid Python identifier. Some common choices for 
# the variable name include x, i, and elem.

# List comprehensions are a concise and efficient way to create 
# lists and perform transformations on sequences of data. 
# They can often be used as a more readable and efficient alternative 
# to traditional loops and list manipulation techniques.

# Here is how you can rewrite the given predicate code using a for loop:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = []

for x in numbers:
    if x % 2 == 0:
        even_squares.append(x**2)

print(even_squares)

# This code will produce the same output as the original code: 
# a list of the squares of the even numbers in the 'numbers' list.

# The for loop iterates over the elements in the 'numbers' list, 
# and the if statement tests each element to see if it is even. 
# If an element is even, it is squared and added to the 'even_squares' 
# list using the append() method.


###### ###### ###### ######- SETS -###### ###### ###### ######
input(bcolors.WARNING + "\nPress 'Enter' to continue to Sets" + bcolors.ENDC)
next_topic()
print(bcolors.HEADER + "\n***SETS***\n" + bcolors.ENDC)

# In Python, a set is an unordered collection of unique elements. 
# Sets are often used to store and manipulate groups of data values, 
# such as the words in a document or the unique elements in a list.

# Here is an example of how to create a set in Python:

s = {1, 2, 3}
print(s)
# prints {1, 2, 3}

# You can also create a set from a list using the set() function:

l = [1, 2, 3, 3, 3, 4, 4, 4]
s = set(l)
print(s)
# prints {1, 2, 3, 4} even though the list contains more elements, they
# are not unique beyond these four values.

# As you can see, the set 's' contains only the unique elements from 
# the list 'l'.

# You can perform various set operations on sets, such as union, 
# intersection, difference, and symmetric difference. 
# Here are a few examples:

# Create two sets
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

# Membership testing
print(3 in s1)  # True
print(7 in s2)  # False
print(7 not in s2) # True

# Set operations
print(s1 | s2)  # Union: {1, 2, 3, 4, 5, 6}
print(s1 & s2)  # Intersection: {3, 4}
print(s1 - s2)  # Difference: {1, 2}
print(s2 - s1)  # Difference: {5, 6}
print(s1 ^ s2)  # Symmetric difference: {1, 2, 5, 6}


# Sets are useful for storing and manipulating data because they 
# are unordered and do not allow duplicate elements. They are also 
# efficient for membership testing and set operations, as they use 
# hash tables to store their elements and perform set operations 
# quickly.

# In Python, sets are implemented using hash tables, which use a 
# hash function to map data to specific locations in the table. 
# The hash function is implemented in C, and is not directly 
# accessible from Python. However, you can see how the hash 
# function is implemented by looking at the Python source code.

# Here is an example of how the hash function is implemented in 
# Python for integers:

# static long
# long_hash(PyLongObject *a)
# {
#     long x;
#     size_t len = Py_SIZE(a);
#     int one_bits;
#     unsigned char *p;

#     /* It's tempting to use Py_SIZE(a) to drive the loop instead of
#        a->ob_size.  However, some bits in ob_size are used to hold
#        the sign of the number, and this sign bit must be excluded
#        from the hash value.  Hence we must use a->ob_digit[0 ..
#        a->ob_size-1] throughout this loop. */
#     x = 0;
#     one_bits = 0;
#     p = (unsigned char*)a->ob_digit;
#     while (len-- > 0) {
#         x = (x<<SHIFT) ^ *p++;
#         one_bits += (x & HASH_BITS) != 0;
#         x &= ~HASH_BITS;
#     }
#     x = x ^ one_bits;
#     if (x == -1)
#         x = -2;
#     return x;
# }


