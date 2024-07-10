single_line = "This is the month of June"

multi_line = '''
This is the month of June.
Today is the 23rd of June.
'''

#indexing with strings
a = "Good morning"
print(a[0])
print(a[6])

#slicing with strings 
print(a[0:4])
print(a[5:])

#slicing with steps [start:stop:step]
print(a[1::3])

#calculating length of a string
for i in range(len(a)):
    print(i)

#string methods
print(a.replace('morning', 'evening'))

print(a.lower())

print(a.upper())

print(a.title())

print(a.lstrip())

print(a.rstrip())

print(a.strip())

b=""
words = ["Hello", "World"]
print(b.join(words))

print(a.isdigit())

print(a.isupper())

print(a.islower())

c = 'hello, {}!'
print(c.format('world'))