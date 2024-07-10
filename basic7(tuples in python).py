tup = (1,2,3,4,5,6,7)

print(tup)

print(tup[3])

print(tup.count(2))

print(tup.index(4))

print(tup[1:4])

#converting list to a tuple
lst = [1,2,3,4,5]
tupl = tuple(lst)

print(tupl)
print(type(tupl))

#converting tuple to a list
tup1 = (3,6,9,12,15)
lst1 = list(tup1)

print(lst1)
print(type(lst1))

lst1.append(18)
print(lst1)

#tuple unpacking
tupp = (1,2,3,4)
a,b,c,d = tupp
print(a)
print(b)
print(c)
print(d)