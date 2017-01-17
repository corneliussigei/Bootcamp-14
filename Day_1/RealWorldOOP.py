class County(object):
    """"
    This class models the
    """
    def __init__(self, name, population):
        self.name = name
        self.population = population

class Demography(County):
    def __init__(self,name, population, geoSize):
        County.__init__(self, name, population)
        self.geoSize = geoSize
    #method to calculate population density
    def calculatePopDensity(self):
        popDensity=self.population/self.geoSize
        return "County Name: " + self.name + ", Population Density: " + str(popDensity)
class Leadership(County):
    def __init__(self, name, population, governor, senator):
        County.__init__(self, name, population)
        self.governor = governor
        self.senator = senator
    def displayPoliticalLeaders(self):
        return "County Name: " + self.name + ", County Governor: " + self.governor + ", County Senator: " + self.senator

county1 = Demography("Nairobi",5200000,14000)
county2 = Leadership("Nakuru", 4500000, "Kinuthia Mbugua", "Joseph Rutto")
print(county1.calculatePopDensity())
print()
print(county2.displayPoliticalLeaders())