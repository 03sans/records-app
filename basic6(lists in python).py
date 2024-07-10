#lists
lst1 = [1,2,3,4,5,6]
lst2 = ["red", "blue", "green"]
lst3 = [1, "Ram", 34.78, "Apple", 5, True]

#indexing in lists
print(lst2[0])
print(lst3[-3])

#slicing in lists
print(lst1[0:3])
print(lst2[-2:])
print(lst3[1:4])

fruits = ['apple', 'banana', 'cranberry']

#updating list
fruits[1]= 'berry'
print(fruits)

#replacing characters in a string
a = fruits[2]
b = a.replace('r', 'b')

print(b)

#adding to a ;list
fruits.append('mango')
print(fruits)

#removing from a list
fruits.remove('cranberry')
print(fruits)

#inserting into a list
fruits.insert(1, 'grapes')
print(fruits)

#sorting a list
fruits.sort()
print(fruits)

#sorted
fruits.sort()
new = sorted(fruits)
print(fruits)
print(new)

#popping from a list
fruits.pop(0)
print(fruits)

#extending a list
more = ['pineapple', 'cherry', 'lemon']
fruits.extend(more)
print(fruits)

#for loop in a list
for fruit in fruits:
    print(fruit)

#while loop in a list
count = 0
while count < len(fruits):
    print(fruits[count])
    count +=1

#2D lists

matrix = [ [1,0,0], [0,1,0], [0,0,1]]
print(matrix[0])
print(matrix[1][2])

for row in matrix:
    for element in row:
        print(element)

#list comprehension
#expression for item in iterable if condition

things = ['pen', 'desk', 'laptop', 'chair', 'wall']
new_things = []
for items in things:
    if items == 'paper':
        new_things.append(items)
print("new list:", new_things)

