#class creates objects(instances) having attributes(varibales) and methods(functions)

class Person:
    a = "Student information"
    def __init__(self, name, age): #constructor of the class 
        self.name = name
        self.age = age

    def greet(self): #method of the class
        print (self.a)
        return f"Hello, my name is {self.name} and I am {self.age} years old"
    
    def gender(self, gen):
        return f"gender: {gen}"


#creating instances(objects) of the person class
person1 = Person('Harry', 17)
gend1 = person1.gender('male')
person2 = Person('Ron', 18)
gend2 = person2.gender('male')

print(person1.name)
print(person1.age)

print(person2.name)
print(person2.age)

print(person1.greet())
print(gend1)
print(person2.greet())
print(gend2)

#class attributes are accessible from everywhere
#object attributes aren't

#inheritance 
#allows one class(child) to inherit attributes and methods from another class(parent)
#1.single inheritance(one to one)

class Car: #superclass
    def color(self):
        return "Red"
    
class ElectricCar(Car): #subclass inheriting superclass
    def battery(self):
        return "Chargeable"
    
newCar = ElectricCar() #subclass object

print(newCar.color())
print(newCar.battery())

#2.multiple inheritance (one to many)

class Annual:
    def fruitA(self, name1):
        return f"{name1} is an annual fruit"
annual1 = Annual()
annual1.fruitA('apple')

class Seasonal:
    def fruitB(self, name2):
        return f"{name2} is a seasonal fruit"
season1 = Seasonal()
season1.fruitB('mango')

class Fruit(Annual, Seasonal):
    def info(self):
        return "Information:"
    
newFruit = Fruit()

print(newFruit.info())
print(newFruit.fruitA('small apple'))
print(newFruit.fruitB('small mango'))

#multilevel inheritance(one to another to another)
class A:
    def method_A(self):
        return "Method A"
    
class B(A):
    def method_B(self):
        return "Method B"
    
class C(B):
    def method_C(self):
        return "Method C"
    
newC = C()

print(newC.method_A())
print(newC.method_B())
print(newC.method_C())

#super()
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth
    
class square(Rectangle):
    def __init__(self, slength):
        super().__init__(slength, slength)

rect = Rectangle (5, 3)
sq = square(4)

print('area of reactangle:', rect.area())
print('area of square:', sq.area())

#abstraction and access specifiers 

#hides the complex implememtation details of a class or object exposing only essential details 

from abc import ABC, abstractmethod 

class Car(ABC):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    @abstractmethod
    def printDetails(self):
        pass

    def accelerate(self):
        print('speed up...')

    def breakApplied(self):
        print('Car stop')

class HatchBack(Car):

        def printDetails(self):
            print('Brand:', self.brand)
            print('Model:', self.model)
            print('Year:', self.year)

        def Sunroof(self):
            print('This feature is unavailable')
        
class Suv(Car):
            
        def printDetails(self):
            print('Brand:', self.brand)
            print('Model:', self.model)
            print('Year:', self.year)

        def Sunroof(self):
            print('Available')

car1 = HatchBack('Maruti', 'Alto', '2022')

car1.printDetails()

#access modifier 

#1.public method: attributes and methods without any leading underscore(_) and can be accessed from anywhere, both within and outside class
'''
class MyClass:
    def __inti__(self):
        self.public_var = 'public attribute'

    def public_method(self):
        return 'this is a public method'
    
obj = MyClass()

print(obj.public_var)
print(obj.public_method())'''


#2.private method: attributes and method with a double underscore(__) prefix are conventionally considered private. they are intended to be accessible only from within the class itself, and their names are 'mangled' to include the class to prevent accidental access from outside the class

class MyClass2:
    def __init__ (self):
        self.__private_var = 'private attribute'

    def __private_method(self):
        return 'this is a private method'
    
obj = MyClass2()

print(obj._MyClass2__private_var)
print(obj._MyClass2__private_method())

#3.protected method: attributes and methods with a leading underscore(_). they shouldnt be accessed directly from outside the class, but can be accessed from wihtin the class and its subclass


#polymorphism: 

#method overloading
class Animal:
    def make_sound(self):
        print('some sound')

class Dog(Animal):
    def make_sound(self):
        print('Bark')
        
class Cat(Animal):
    def make_sound(self):
        print('Meow')

dog = Dog()
cat = Cat()

dog.make_sound()
cat.make_sound()