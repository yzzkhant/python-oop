class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender    

    def success(self):
        print(self.name, "is successful")
    def failure(self):
        print(self.name, "is failure")
    def fight(self):
        print(self.name, "is fighting")

Human1 = Human("Alice", 25, "Female")
Human2 = Human("Bob", 30, "Male")

Human1.success()
Human2.failure()
Human1.fight()