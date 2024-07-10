#sum of all the elements in a 2D list
newList = [[1,2,3],[4,5,6],[7,8,9]]
sum = 0
for i in newList:
    for j in i:
        sum = sum + j
print(sum)

#list comprehension
num = [1,2,3,4,5,6,7,8,9,10]
odds = []
evens = []

for k in num:
    if k%2 == 0:
        evens.append(k)
    else:
        odds.append(k)
print(odds)
print(evens)

numlst = [1,2,3,4,5,6,7,8]
evenlst = []

