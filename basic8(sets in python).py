sett = {1,2,3,4,5}

#creating an empty set
a = set()

#adding values to a set
a.add(1)
print(a)

sett.add(6)
print(sett)

#removing values from a set
a.remove(1)
print(a)

sett.remove(6) #method shows error if element not present in set
print(sett)

#discarding from a set
sett.discard(4) #method doesnt show error even if element is not present in set
print(sett)

#set operations
A = {1,2,4,6,8,10}
B = {1,3,5,7,8,9}

print(A|B)#union
print(A & B)#intersection
print(A - B)#difference
print(A ^ B)#symmetric difference 

#set operations using strings
color = {'red', 'orange', 'peach', 'green'}
fruit = {'orange', 'peach', 'banana', 'mango'}

print(color|fruit)#union
print(color & fruit)#intersection
print(color - fruit)#difference
print(color ^ fruit)#symmetric difference 

#frozenset
set1 = {1,11,111,1111}
fs = frozenset(set1)
print(fs)

