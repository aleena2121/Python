class Player:
    def __init__(self,name,age,height,weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    
    def get_age(self):
        print(f"{self.name} is {self.age} years old ")

    def get_height(self):
        print(f"{self.name} is {self.height}cm")

    def get_weight(self):
        print(f"{self.name} weighs {self.weight}kg")

p1 = Player("David Jones",25,175,75)
p1.get_age()
p1.get_height()
p1.get_weight()