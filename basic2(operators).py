'''#comparsion operators using interger
a = 5
b = 7

print("Equal to:", a == b)
print("Not equal to:", a != b)
print("Greater than:", a > b)
print("Less than:", a < b)
print("Greater than or equal to:", a >= b)
print("Less than or equal to:", a <= b)

#comparison operators using strings

c = "John"
d = "Mary"

print("Equal to:", c == d)
print("Not equal to:", c != d)

#logical operators 
x = True
y = False

print("Logical AND:", x and y)
print("Logical OR:", x or y)
print("Logical NOT:", not x)

#membership operator 
lst = [1,2,3,4,5]

print("membership (in):", 3 in lst)
print("membership (not in):", 7 in lst)

#identity operator 
e = [1,2,3]
f = ["a", "b", "c"]
g = e 

print("identity (is):", e is g)
print("identity (is not):", f is g)

#assignment operator 
num = 100

num &= 101 #bitwise operator(for binary operations)
print(num)

num += 1
num -= 1
num *= 1
num /= 1
num //= 1
num %= 1
num **= 1

name = 1
a = str(name)
a = input("enter a number: ")

print("value of a: ", a)

s = {1,1,2,3,4,4,5}
print(s)

#numeric 
num1 = 3
num2 = 3.14

#string
name = "John"

#complex
x = 1j

#list
lst = [1,1,2,3,5,6,5,"rose","maple"]

#tuple
t = ("apple","ball")

#range
x = range(3)

#dictionary 
d = {'id': 1, 'name' : 'Ram', 'age' : 27}

#set 
set_num = {1,2,3,4,5}

#frozen set
x = fronzenset({1,2,3,4,5})

#boolean 
isValid = False

#none 
value = None

#getting data type
a = "Rita"
b = 2

print(type(a))
print(type(b))'''

