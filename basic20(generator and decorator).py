def counting(max):
    count= 1
    while count <= max:
        yield count
        count += 1

counter = counting (5)

for num in counter:
    print(num)

def fibo():
    a,b = 0,1
    while True:
        yield a
        a,b = b, a+b

fib = fibo()
for _ in range(10):
    print(next(fib))

def my_decorator(func):
    def wrapper():
        print("this is a sentence")
        func()
        print('this is another sentence')
    return wrapper

@my_decorator
def say():
    print('hello!')

say()