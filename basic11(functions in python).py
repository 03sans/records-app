'''def function_name(parameters):
    docstring
    function body 
    use parameters to perform operation
    return expression'''

#function_name() calling a function


def addNumbers(a,b):
    print(a)
    print(b)
    s = a+b
    return s

returnValue = addNumbers(4,2)
print(returnValue)

def stringAdd(x,y):
    print(x)
    print(y)
    z = x+y
    return z

returning = stringAdd("HELLO", "WORLD")
print(returning)

def get_stats(numbers):
    min_value = min(numbers)
    max_value = max(numbers)
    sum_value = sum(numbers)
    return min_value, max_value, sum_value

numbers = [1,2,3,4,5,6]
min_value, max_value, sum_value = get_stats(numbers)

print("Minimum", min_value)
print("Maximum", max_value)
print("Sum", sum_value)

def get_stats(numbers):
    min_value = min(numbers)
    max_value = max(numbers)
    sum_value = sum(numbers)
    lst = [min_value, max_value, sum_value]
    return lst

numbers = [1,2,3,4,5,6]
val = get_stats(numbers)

print(val)

def get_stats(numbers):
    return {
        'min': min(numbers),
        'max': max(numbers),
        'sum': sum(numbers)
    }

numbers = [1,2,3,4,5,6]
stats = get_stats(numbers)

print('minimum', stats['min'])
print('maximum', stats['max'])
print('sum', stats['sum'])

def greet(name, greeting = "Hola"):#default argument
    print(f"{greeting}, {name}")

greet("Juan")
greet("Alison", "Bonjour")

def sub_numbers(s,t):
    return s-t

val = sub_numbers(10,5)
print(val)

def newFunction():
    a = 1  #a is a local variable, only accessible within a function 
    print(a)

newFunction()

disc = 100 #Global variable, accessible inside as well as outside a function

def newDisc():
    print(disc)

newDisc()

def func():
    global x
    x = 2
    print(x)

func()
print(x)

def myFunc(*args,**kargs):
    for i in args:
        print(i)
    print(kargs['name'])

myFunc(1,2,3,4,5,6,7, name='sita')
