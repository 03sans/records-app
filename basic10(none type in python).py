#is operator
x = None
y = None

print(x is None)
print(y is None)

z = 5

print(z is None)

#use case for none
def print_message(message):
    if message:
        print(message)
    else:
        return None

result = print_message("hello")
print(result)