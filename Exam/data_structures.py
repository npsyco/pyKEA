###### ###### ###### ######- LISTS -###### ###### ###### ######

print("\n***LISTS***\n")

# In Python, a list is an ordered collection of items that 
# can be of any data type, including other lists. Lists are 
# used to store and manipulate data in a structured way.

# Here is an example of how to create a list in Python:

l = [1, 2, 3, 4, 5]
print(l)
# prints [1, 2, 3, 4, 5]

# In this example, we create a list 'l' that contains five integers.

# You can access the elements of a list using indexing:

print(l[0])  # 1
print(l[1])  # 2
print(l[2])  # 3
print(l[3])  # 4
print(l[4])  # 5

# You can also use negative indexing to access the elements of a 
# list from the end:

print(l[-1])  # 5
print(l[-2])  # 4
print(l[-3])  # 3
print(l[-4])  # 2
print(l[-5])  # 1

# You can modify the elements of a list by reassigning them:

l[0] = 10
print(l)  # [10, 2, 3, 4, 5]

l[1] = 20
print(l)  # [10, 20, 3, 4, 5]

# You can use slicing to access a range of elements:

print(l[2:3]) # [3]

# You can modify the amount of jumps during slicing:

print(l[0:5:2]) # [10, 3, 5]

# You can reverse the entire list, with the integer defining 
# number of jumps:

print(l[::-2]) # [5, 3, 10]

# You can concatenate the list:

l2 = [6 ,7]
lx = l + l2
print(lx)

# Or by using the keyword .extend()

l3 = [8, 9]
l.extend(l3)
print(l)

# You can get the length of iterable elements of a list:

print(len(l))

# You can display the minimum and maximum values in a list:

print(min(l))
print(max(l))

###### ###### ###### ######- DICTIONARIES -###### ###### ###### ######

print("\n***DICTIONARIES***\n")

# In Python, a dictionary is a collection of key-value pairs. 
# Dictionaries are used to store and manipulate data that is 
# organized into pairs of keys and values.

# Here is an example of how to create a dictionary in Python:

d = {'a': 1, 'b': 2, 'c': 3}
print(d)
# prints {'a': 1, 'b': 2, 'c': 3}

# In this example, we create a dictionary 'd' that contains three 
# key-value pairs. The keys are 'a', 'b', and 'c', and the 
# corresponding values are 1, 2, and 3.

# You can access the values in a dictionary using the keys:

print(d['a'])  # 1
print(d['b'])  # 2
print(d['c'])  # 3

# You can also modify the values in a dictionary by reassigning them:

d['a'] = 10
print(d)  # {'a': 10, 'b': 2, 'c': 3}

d['b'] = 20
print(d)  # {'a': 10, 'b': 20, 'c': 3}

d['c'] = 30
print(d)  # {'a': 10, 'b': 20, 'c': 30}

# You can add new key-value pairs to a dictionary using the 
# assignment operator:

d['d'] = 40
print(d)  # {'a': 10, 'b': 20, 'c': 30, 'd': 40}

# You can delete key-value pairs from a dictionary using the 'del' 
# statement:

del d['a']
print(d)  # {'b': 20, 'c': 30, 'd': 40}


###### ###### ###### ######- TUPLES -###### ###### ###### ######

print("\n***TUPLES***\n")

# In Python, a tuple is an immutable sequence type, while a set 
# is an unordered collection of unique elements. Here are some 
# key differences between tuples and sets:

# Immutability: As mentioned earlier, tuples are immutable, 
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

# Tuples can contain elements of different types, 
# including other tuples:

t = (1, 'a', 3.14, (5, 6))
print(t)

# You can access the elements of a tuple using indexing, 
# just like you would with a list:

# Create a tuple
t = (1, 2, 3, 4, 5)

# Access the elements of the tuple using indexing
print(t[0])  # 1
print(t[1])  # 2
print(t[2])  # 3
print(t[3])  # 4
print(t[4])  # 5

# You can also use negative indexing to access the elements of the tuple
print(t[-1])  # 5
print(t[-2])  # 4
print(t[-3])  # 3
print(t[-4])  # 2
print(t[-5])  # 1

# You can also use slicing to access a range of elements in a tuple:

t = (1, 2, 3, 4, 5)
print(t[1:3])
# prints 2 and 3

# One of the main advantages of tuples is that they are immutable, 
# which means they are less prone to accidental modification and 
# can be used as keys in dictionaries and elements in sets. 
# Tuples are also generally faster and use less memory than lists, 
# making them a good choice for storing large amounts of data.

# Here's an example of using a tuple as a key in a dictionary, 
# as long as the tuple is immutable (i.e., it contains only 
# immutable elements such as strings, numbers, or other tuples).

# Create a dictionary with a tuple as the key
d = {(1, 2): 'a', (3, 4): 'b', (5, 6): 'c'}

# Access the values in the dictionary using the tuple keys
print(d[(1, 2)])  # 'a'
print(d[(3, 4)])  # 'b'
print(d[(5, 6)])  # 'c'


###### ###### ###### ######- LIST COMPREHENSION -###### ###### ###### ######

print("\n***LIST COMPREHENSION***\n")

# List comprehension is a concise way to create a list using a 
# single line of code. It is often used to perform a transformation 
# or computation on a sequence of input values and return the 
# resulting list.

# Here is an example of a basic list comprehension:

numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers] # x or i
print(squares)
# prints [1, 4, 9, 16, 25]

# In this example, the list comprehension [x**2 for x in numbers] 
# iterates over the numbers list and creates a new list squares 
# that contains the squares of each number in numbers.

# List comprehensions can also include an optional conditional 
# expression, known as a predicate, that filters the input values 
# based on a certain condition. For example:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = [x**2 for x in numbers if x % 2 == 0]
print(even_squares)
# prints [4, 16, 36, 64, 100]

# In this example, the list comprehension 
# [x**2 for x in numbers if x % 2 == 0] iterates over the numbers 
# list and creates a new list even_squares that contains the 
# squares of only the even numbers in numbers.

# In Python, the variable x is often used as a convention for list 
# comprehensions, but you can use any variable name that you like. 
# The variable name x is used to represent each element in the input 
# list or iterable, and is typically used to make the list 
# comprehension more readable.

# Here is an example of using the variable i instead of x in a list 
# comprehension:

# Create a list of squares using list comprehension
squares = [i**2 for i in range(1, 11)]
print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# In this example, we use the variable i to represent each element 
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
# a list of the squares of the even numbers in the numbers list.

# The for loop iterates over the elements in the numbers list, 
# and the if statement tests each element to see if it is even. 
# If an element is even, it is squared and added to the even_squares 
# list using the append() method.


###### ###### ###### ######- SETS -###### ###### ###### ######

print("\n***SETS***\n")

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


