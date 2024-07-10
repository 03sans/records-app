#empty dictionary
empty = {}

dict = {'s.n': 1, 'name': 'John', 'address': 'Florida'}
print(dict['name'])
print(dict.get('name'))

#modifying and adding elements
dict['name'] = 'Jane'#modifying
print(dict)

dict['gender'] = 'Female'#adding
print(dict)

#removing elements
del dict['gender']
print(dict)

#popping elements
a = dict.pop('s.n')
print(a)

#dictionary methods
dictt = {'id': 1, 'name': 'Shiela', 'age': 24, 'address': 'London', 'employeed': 'full time'}

print(dictt.keys())
print(dictt.values())
print(dictt.items())
#print(dictt.clear())

for i in dictt:
    print(i, ':', dictt[i])

#nested dictionary
student = {'name': 'Jake', 'age': '18', 'grades': {'maths': 90,
            'english': 94}, 'contact': {'phone': '9800000000', 'email': 'xyz@gmail.com'}}

print(student['name'])
print(student['grades']['english'])
print(student['contact']['email'])

#creating a 2D dictionary
colors = {}
colors['desk']='brown'
colors['fan']='black'
colors['lamp']='white'
print(colors)

things = {}
things['object']= 'table'
things['colors']=colors
print(things)

#dictionary comprehensions
words = ['apple','banana', 'cherry']
word_lengths = {word: len(word) for word in words}

print(word_lengths)

word_lengths = {word:len(word) for word in words if word == 'apple'}
print(word_lengths)


