class PartyAnimal:
    x = 0
    name = ""

    def __init__(self, name):
        self.name = name
        print self.name, "constructed"

    def party(self):
        self.x = self.x + 1
        print "So far", self.x


s = PartyAnimal("Sally")
s.party()
s.party()
s.party()
PartyAnimal.party(s)
print "Type", type(s)
print "Dir", dir(s)

j = PartyAnimal("Jim")
j.party()
s.party()
s.party()
