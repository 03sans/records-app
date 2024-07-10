class Vehicle: #superclass
    def __init__(self, brand, model):
        self.brand = brand   #public    
        self._model = model   #protected   
        self.__vehicle_type = "non-electric" #private

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self._model}")
        print(f"Vehicle Type: {self.__vehicle_type}")

class Car(Vehicle): #subclass1
    def __init__(self, brand, model, seating_capacity):
        super().__init__(brand, model)
        self.seating_capacity = seating_capacity 

    def display_car_info(self):
        self.display_info()  
        print(f"Seating Capacity: {self.seating_capacity}")

class Bike(Vehicle): #subclass2
    def __init__(self, brand, model, bike_type):
        super().__init__(brand, model)
        self.bike_type = bike_type 

    def display_bike_info(self):
        self.display_info()  
        print(f"Bike Type: {self.bike_type}")

#class Vehicle1(Car, Bike):


car = Car("Maruti", "Suzuki", 5) #subclass1 object
bike = Bike("Pulsar", "Shine", "Petrol") #subclass2 object

car.display_car_info()
print('-'*25)
bike.display_bike_info()
print('-'*25)

#acessing public attributes
print(f"Car's Brand: {car.brand}")  
print(f"Bike's Brand: {bike.brand}")  

#accessing protected attributes
print(f"Car's Model: {car._model}")  
print(f"Bike's Model: {bike._model}")  

#accessing private attributes
'''print(car.__vehicle_type)  
print(bike.__vehicle_type)''' 
