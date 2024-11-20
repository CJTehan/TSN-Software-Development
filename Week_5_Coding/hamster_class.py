class Hamster:
    def __init__(self, name, colour, hunger=70, energy=30):
        self.name = name
        self.colour = colour
        self.hunger = hunger
        self.energy = energy
    def eating(self, food):
        print(f"{self.name} is enjoying some {food}")
        print("*munch munch*")
        self.hunger = max(self.hunger - 50, 0)
        print(f"{self.name}'s hunger is about {self.hunger}%")
    def playing(self):
        print(f"{self.name} is playing!")
        print(f"{self.name} has the zoomies")
        self.energy = max(self.energy - 40, 0)
        self.hunger = min(self.hunger + 20, 100)
        print(f"{self.name}'s energy is now {self.energy}% and hunger is {self.hunger}%")
    def sleeping(self):
        print(f"{self.name} is catching some zzz's")
        print("zzz...zzz...")
        self.energy = min(self.energy + 60, 100)
        self.hunger = min(self.hunger + 10, 100)
        print(f"{self.name}'s energy is now {self.energy}% and hunger is {self.hunger}%.")
    def status(self):
        print(f"{self.name}'s Status:")
        print(f"Colour: {self.colour}")
        print(f"Hunger: {self.hunger}%")
        print(f"Energy: {self.energy}%")
        print("")
hamster1 = Hamster(name="Pikachu", colour="Yellow")
hamster2 = Hamster(name="Hammy", colour="Brown")
hamster1.status()
hamster1.eating("Berry")
hamster1.playing()
hamster1.sleeping()
hamster1.status()
hamster2.status()
hamster2.eating("Carrot")
hamster2.eating("Walnut")
hamster2.sleeping()
hamster2.playing()
hamster2.status()