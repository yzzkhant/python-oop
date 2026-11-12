class Car:

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start(self):
        print(self.brand, "is starting")
        
        
car1 = Car("Toyota", "Red")
car2 = Car("BMW", "Black")

print(car1.brand)
print(car2.brand)

car1.start()
car2.start()