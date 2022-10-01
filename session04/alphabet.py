# Modules and List Comprehensions

# Ex. 1: Alphabet List Comprehensions

# 1. Create a list of capital letters in EN alphabet
from hashlib import new
import string
print("Ex. 1 - TASK ONE")

alphabet_caps = list(string.ascii_uppercase)
print(alphabet_caps)

# 2. Create a list of capital letters from the EN alpha,
# exclude 4 with Unicode point of either 70, 75, 80, 85
print("Ex. 1 - TASK TWO")
alphabet_caps1 = list(string.ascii_uppercase)

for i in alphabet_caps1:
    # print(ord(i))  
    if ord(i) == 70:
        print(ord(i))
        alphabet_caps1.remove(i)
    elif ord(i) == 75:
        print(ord(i))
        alphabet_caps1.remove(i)
    elif ord(i) == 80:
        print(ord(i))
        alphabet_caps1.remove(i)
    elif ord(i) == 85:
        print(ord(i))
        alphabet_caps1.remove(i)
    
print(alphabet_caps1) 
    
# 3. Create a list of capital letters from the EN alpha, 
# exclude every second between F & O

print("Ex. 1 - TASK THREE")
alphabet_caps2_list = list(string.ascii_uppercase)
#print(alphabet_caps2_list)
def get_alpha_letters(start, stop, step):
    for char in range(ord(start.upper())+1, ord(stop.upper())+1, step):
        yield chr(char)
excluded_letters = list(get_alpha_letters("h", "o", 2)) #works
alphabet_caps2_set = set(alphabet_caps2_list)
excluded_letters_set = set(excluded_letters)
print(alphabet_caps2_set - excluded_letters_set)

# Ex 2: Clothes List Comprehension
print("Ex. 2 - TASK 1")
# 1. From 2 lists, using a list comprehension, create a list containing:

# [(‘Black’, ‘s’), (‘Black’, ‘m’), (‘Black’, ‘l’), (‘Black’, ‘xl’), 
# (‘White’, ‘s’), (‘White’, ‘m’), (‘White’, ‘l’), (‘White’, ‘xl’)]

colors = ['Black', 'White']
sizes = ['s', 'm', 'l', 'xl']

mix = [(i, j) for i in colors for j in sizes]
print(mix)

# Ex 2: 
# 2. If the tuple pair is in the following list, it should not be 
# added to the comprehension generated list.
# (black, m), (white, s)
print("Ex. 2 - TASK")

mix_minus = [(i, j) for i in colors for j in sizes 
# if i != "Black" and j != "m" or i != "White" and j != "s"]
# why does above remove (black, s) and (white, m)???
if i != "Black" and j != "s" or i != "White" and j != "m"]
print(mix_minus)