import time

class Bot:
    def __init__(self, name, age, energy, shield, summary):
        self.name = name
        self.age = age
        self.energy = energy
        self.shield = shield
        self.summary = summary

    def display(self):
        print("{} is {} years old".format(self.name, self.age))
        print("{} has {} energy".format(self.name, self.energy))
        print("{} has {} shield".format(self.name, self.shield))
        print("{} has {} attributes".format(self.name, self.summary))

    def display_name(self):
        print("x"+len(self.name)*"x"+"x")
        print("x{}x".format(self.name))
        print("x"+len(self.name)*"x"+"x")

    def display_age(self):
        print("{}  {} ".format(self.name, self.age))
       



charlie = Bot("Charlie",4545, 5, 5, 5)

charlie.display_name()
charlie.display()

charlie.display_age()



