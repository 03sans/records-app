'''lst = [1,2,3,4,5]

for i in lst:
    print(i)

a = ['a', 'b', 'c']

for j in a:
    print(j)

lst = ['ram', 'shyam', 1, 3, 'hari', 5, 6]

for i in lst:
    if type(i) == str:
        print("string")
    elif type(i) == int:
        print("integer")
    else:
        print("invalid")

name = "Sanskriti1"

for i in name:
    if i == '1':
        print(i)
    else:
        print("not integer")

dictt = {'id': 1, 'name': 'ram'}
for i in dictt.items():
    print(i)


dict1 = {'id': 1, 'name': 'hari', 'age': 20}
for key, values in dict1.items():
    print("this is the key", key)
    print("this is the value", values)

for a in range(2, 10, 3):
    print(a)

lst1 = [1,2,3,4,5,6,7,8,9]

for i in range(len(lst1)):
    print(i)

'''

'''#iteration through while loop

count = 0 
while count < 5:
    print(count)
    count += 1'''

'''#swapping values
a, b = 10, 20
a, b = b, a
print(a, b)

x = 2
y = 4
z = x
x = y
y = z
print(x, y)

s = 5
t = 10
s = s+t
t = s-t
s = s-t
print(s,t)'''

#break statement
'''
num = [1,2,3,4,5]
for i in num:
    if i == 4:
        break
    print(i)'''

'''val = ['ram', 1, 'shyam', 2, 'hari', 3]
for i in val:
    if i == 3:
        continue
    print(i)

lst2 = [1,2,3,4,5]
for j in lst2:
    if j == 4:
        print("xyz", j)
        continue
    print("abc", j)'''

i = 0
while i < 5:
    i += 1
    if i == 4:
        continue 
    print(i)

j = 0
while j < 10:
    j += 2
    if j == 6:
        break
    print(j)

