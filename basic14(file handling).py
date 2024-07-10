'''with open('sample.txt', 'r') as file:
    a = file.read()
    print('reading the file content')
    print(a)

with open('sample.txt', 'w') as file:
    a = file.write('I am writing in the file')
    print('reading the file content')
with open('sample.txt', 'r') as file:
    a = file.read()
    print(a)

with open('sample.txt', 'w+') as file:
    a = file.write('I am writing in the file\n This is some text')
    print('reading the file content')
    
with open('sample.txt', 'r') as file:
    a = file.readline()
    print(a)
    a = file.readline()
    print(a)


with open('sample.txt', 'r') as file:
    a = file.readlines()
    print(a)
    lst = []
    for x in a:
        value = x.strip('\n')
        print(value)
        lst.append(value)
    
    print(lst)


file = open('sample.txt', 'r')
a = file.read()
print(a)
file.close()

file_path = 'sample.txt'
with open(file_path, 'a') as file:
    file.write('appending \n')

file_path = 'sample.txt'
with open(file_path, 'w') as file:
    file.write('hello \n')

try:
    with open('sample.txt', 'r') as file1, open ('sample2.txt', 'w') as file2:
        a = file1.readlines()
        print(a)
        lst =[]
        for x in a:
            value = x.strip('\n')
            print(value)
            lst.append(value)

        file2.writelines(lst)

except FileNotFoundError:
    print("file doesn't exist")

import csv

file_path = 'data.csv'

with open(file_path, mode = 'r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    for row in csv_reader:
        print(row)

import csv

data = [
    ['alice', 30, 'london'],
    ['bob', 25, 'paris'],
    ['charlie', 35, 'berlin']
]

file_path = 'data2.csv'
with open(file_path, mode = 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['Name', 'Age', 'Address'])
    for row in data:
        csv_writer.writerow(row)

import csv

file_path = 'data2.csv'

with open(file_path, mode = 'r')as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row)
        print(row['Name'], row['Age'], row['Address'])'''

import csv

data = [
    {'Name': 'Alice', 'Age': 20, 'Address': 'London'},
    {'Name':'Bob', 'Age': 23, 'Address': 'Chelsea'}
]

file_path = 'data3.csv'
fieldnames = ['Name', 'Age', 'Address']

with open(file_path, mode = 'w')as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for row in data:
        writer.writerow(row)