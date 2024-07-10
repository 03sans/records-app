#odd, eve, zero using for loop
lst = [0,1,2,3,4,5,6,7,8,9]

for i in lst:
    if i%2 == 0:
        print(i, "is even")
    elif i%2 !=0:
        print(i, "is odd")
    else:
        print("zero")

#prime or composite using while loop
num = int(input("enter a number:"))

a = 2
count = 0
while num > a:
    if num%a == 0:
        count = 1
    a = a + 1
if count == 0:
    print(num, "is prime")
else:
    print(num, "is composite")

#numbers divisible by 5 using for loop and continue 
lst2 = [5,10,2,15,25,4,30]

for i in lst2:
    if i%5 == 0:
        print(i, "is divisible by 5")
    else:
        continue 

#printing name using while loop
name = input("Enter name:")
b = 0

while b < 10:
    print(name)
    b += 1
    if b == 5:
        break