# 1. Model of org - 3 sets
print("-------Part 1-------")

board = {"Benny", "Hans", "Tine", "Mille", "Torben", "Troels", "Søren"}
mgnt = {"Tine", "Trunte", "Rane"}
employees = {"Niels", "Anna", "Tine", "Ole", "Trunte", "Bent", "Rane", "Allan", "Stine", "Claus", "James", "Lars"}

# On board, !employee
print(board - employees)

# On board, also employee
print(board & employees)

# How many in mngt, also board
print(len(mgnt & board))

# All Mngt, also employee
print(employees & mgnt)

# All mngt, also on board
print(mgnt & board)
# Member of all
print(mgnt & board & employees)

# Employees, not mngt nor board
print(employees - board - mgnt)


# 2. From list comprehension, make list of tuples from {'a': 'Alpha',...}
print("\n-------Part 2-------")

letters = ["a", "b", "g"]
greek = ["Alpha", "Beta", "Gamma"]
data_tuple = list(zip(letters, greek))
print(data_tuple)

# 3. From 2 sets create

print("\n-------Part 3-------")

set1 = {'a', 'e', 'i', 'o', 'u', 'y'}
set2 ={'a', 'e', 'i', 'o', 'u', 'y', 'æ' ,'ø', 'å'}

# Union
print(set1 | set2)

# Symmectric Difference
print(set1 ^ set2)

# Difference
print(set2 - set1)

# Disjoint
print(set1.isdisjoint(set2))

# 4. Date decoder. Convert dd-MMM-yy to y, m, d
print("\n-------Part 4-------")

months = {
    "jan": "1",
    "feb": "2",
    "mar": "3",
    "apr": "4",
    "may": "5",
    "jun": "6",
    "jul": "7",
    "aug": "8",
    "sep": "9",
    "oct": "10",
    "nov": "11",
    "dec": "12"
}

def dateConv(s):
    list(months.values())
    s = s.split("-")
    m = months.get(s[1])
    res = ( s[2], m, s[0] )
    resC = ""
    for i in res:
        resC = resC + i + "/"
    # should remove last /

    print(resC)

dateConv(input("Enter date(dd-MMM-yy): "))