from bot.py import Bot

class SuperBot(Bot):
    def __init__(self, name, age, energy, shield, super_power):
        self.name = name
        self.age = age
        self.energy = energy
        self.shield = shield
        self.summary = summary
        super().__init__(name, age, energy, shield)
        self.employee_id = employee_id

    def display_superbot(self):
        print(self.employee_id)
