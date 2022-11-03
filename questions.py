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
# and below removes correctly: (black, m), (white, s)
if i != "Black" and j != "s" or i != "White" and j != "m"]
print(mix_minus)