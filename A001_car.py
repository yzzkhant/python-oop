class Car:
    def __init__(self, color, wheels, brand, model):
        self.color = color
        self.wheels = wheels
        self.brand = brand
        self.model = model
        
    def drive(self):
        print("Car is driving")
        
    def stop(self):
        print("Car has stopped")
        
car1 = Car("Red", 4, "Toyota", "Camry")
car2 = Car("Blue", 4, "Honda", "Civic")

print(car1.color) # Output: Red
print(car2.brand) # Output: Honda
print(car1)

class Car:
    def __init__(self, color, wheels, brand, model):
        self.color = color
        self.wheels = wheels
        self.brand = brand
        self.model = model
        
    def drive(self):
        print("Car is driving")
    
    def stop(self):
        print("Car has stopped")

Car1 = Car("Red", 4, "Toyota", "Camry")
Car2 = Car("Blue", 4, "Honda", "Civic")

print(Car1.color) # Output: Red
print(Car2.brand) # Output: Honda
