class Bot:
    def __init__(self, name, age, energy, shield, summary):
        self.display_name = name
        self.display_age = age
        self.display_energy = energy
        self.display_shield = shield
        
        
    def display(self):
        print("{} is {} years old".format(self.name, self.age))
        print("{} has {} energy".format(self.name, self.energy))
        print("{} has {} shield".format(self.name, self.shield))
        print("{} has {} attributes".format(self.name,self.summary))
        
charlie = Bot("Charlie", 4545, 85, 5, 6)

charlie.display()
    