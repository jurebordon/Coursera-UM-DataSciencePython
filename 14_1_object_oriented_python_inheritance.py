class PartyAnimal:
    x = 0
    name = ""

    def __init__(self, name):
        self.name = name
        print self.name, "constructed"

    def party(self):
        self.x = self.x + 1
        print "So far", self.x


class FootballFan(PartyAnimal):
    points = 0

    def touchdown(self):
        self.points = self.points + 1
        self.party()
        print self.points, "points"


s = PartyAnimal("Sally")
s.party()

j = FootballFan("Jim")
j.party()
j.touchdown()
