'''#lambda functions(anonymous functions):small, anon defined using lambda keyword, can have any no of arguments but only one expression, which is evaluated and returned
#lambda arguments: expression

square = lambda x: x ** 2
print(square(5))

add = lambda a, b: a + b
print(add(5,7))

#map(): applies to all the items in an input list(or other iterable), returns a map obj(an iterator) that yields results of applying the function to each item of the iterable
#map(function, iterable)
lst = [1,2,3,4,5,6]

def fun(a):
    a += 1
    return a

new= list(map(fun, lst))
print(new)

num = [1,2,3,4,5]
sq = list(map(lambda x:x ** 2, num))
print(sq)

#filter():constructs an iterator from elements of an iterable for which a function returns true
#filter(function,iterable)

numb = [1,2,3,4,5,6,7,8,9,10]
ev = list(filter(lambda x:x % 2==0,numb))
print(ev)

lst2 = [1,3,5,10,13,16,15,20]

def func(b):
    if b % 5 == 0:
        return b
    
neww = list(filter(func, lst2))
print(neww)

#reduce():repeatedly applies a function to pairs of elements from left to right until only one value remains
#functools.reduce(function, iterable[,initializer])


from functools import reduce

numbers = [1,2,3,4,5]
sum = reduce(lambda x,y:x+y,numbers)
print(sum)

numbers = [3,8,1,6,2]
max_num = reduce(lambda x,y:x if x > y else y, numbers)
print(max_num)

words = ['hello', ' ', 'world', '!']
sentence = reduce(lambda x,y:x+y, words)
print(sentence)

numbers = [1,2,3,4,5]
product = reduce(lambda x,y:x * y, numbers, 2)
print(product)

#os library :provides functions for interacting with the os, such as managing files and directories

import os
current_dir = os.getcwd()
print(current_dir)

files = os.listdir(current_dir)
print(files)

new_dir = 'new directory'
os.mkdir(new_dir)
print(f"created directory '{new_dir}")

path_to_check = new_dir
if os.path.isdir(path_to_check):
    print(f'{path_to_check} is a directory')
elif os.path.isfile(path_to_check):
    print(f'{path_to_check} is a file')
else:
    print('error')

os.chdir(new_dir)
print('changed to:', os.getcwd())

new_dir_files = os.listdir()
print(new_dir_files)
'''
#random library:provides functions for generating random numbers, selecting random elements and more

import random 
ran_num = random.randint(1,10)

my_list = [1,2,3,4,5]
random.shuffle(my_list)
print(my_list)

print(random.random)
print(random.randint(1,20))
print(random.choice(['apple','ball','cat']))

lst3 = [1,2,3,4,5]
random.shuffle(lst3)
print(lst3)

popu = range(1,11)
sample = random.sample(popu, 5)
print(sample)

#math library: provides mathematical functions defined by the c standard

import math
sqr = math.sqrt(25)
facto = math.factorial(5)

print(sqr)
print(facto)

print('sin(pi/2):', math.sin(math.pi/2))
print('exp(1):', math.exp(1))
print('log(e):', math.log(math.e))
print('log10(10):', math.log10(10))
print('2^3:', math.pow(2,3))
