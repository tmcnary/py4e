class PartyAnimal:
    x = 0
    def party(self):
        self.x = self.x + 2
        print(self.x)

an = PartyAnimal()
an.party()
an.party()

class HotDog:
    x = 0
    def glizzy(self):
        self.x = self.x + 1
        print(self.x)

hd = HotDog()
hd.glizzy()

class HotDog:
    x = 0
    def glizzy(self):
        self.x = self.x + 1
        print(self.x)
        
HotDog(glizzy())
HotDog.glizzy()