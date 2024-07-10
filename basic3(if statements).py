'''#type validation 
value = input("enter a number:")

if value.isdigit():
    num = int(value)
    print(f"Converted to integer: {num}")
elif '.' in value:
    num = float(value)
    print(f"Converted to float: {num}")
else:
    print("Invalid number input")'''

'''#number type with conditionals
number = int(input("enter a number:"))

if number > 0 :
    print(f"The number {number} is a positive number")
elif number < 0:
    print(f"The number {number} is a negative number")
else:
    print("The number is equal to zero")
'''
'''#string type with conditionals
fruit = input("Enter a fruit:")

if fruit.lower() == "apple":
    print(f"{fruit} is a annual fruit")
elif fruit.lower() == "mango":
    print(f"{fruit} is a seasonal fruit")
else:
    print("Enter a valid input")'''

'''#chained conditionals
a = 14
if a < 15: 
    print("a is less than 15")
if a > 10:
    print("a is greater than 10")

x = 2
if x < 5:
    x += 2
    print(f"x is greater than 5: {x}")
if x > 15:
    print("x is less than 15")'''

#nested conditionals 
'''a = int(input("Enter a number:"))
if a > 0:
    if a < 10:
        print(f"The number {a} is a positive single digit number")
    else:
        print(f"The number {a} is positive but not a single digit number")
else:
    print(f"The number {a} is not a positive number")'''

'''num = input("Enter a number:")
if num.isdigit():
    b = int(num)
    if b > 0:
        print("positive number")
    elif b < 0:
        print("negative number")
    else:
        print("zero")
else:
    print("invalid input")'''

'''x = input("enter a value:")

new = int(x)
print(type(new))
if  new > 5 or new < 10 and new/2 == 1:
    print(new)
else:
    print("invalid")'''

fruit = (1,2,3,4,5,6)
value = fruit*2
print(value)

#type(variable) == str (checks if the variable is string or not)

#recursion 
#factorial function

