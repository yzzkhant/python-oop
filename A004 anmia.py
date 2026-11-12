class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def make_sound(self):
        print(self.name, "makes a sound")
    def bite(self):
        print(self.name, "bites")
    def eat(self):
        print(self.name, "eats food")
        
animal1 = Animal("Dog", "Canine")
animal2 = Animal("Cat", "Feline")

animal1.make_sound()
animal2.bite()