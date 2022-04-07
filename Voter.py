import random

class Voter():
    def __init__(self, probRepublican, probDemocrat) :
        self.probRepublican = probRepublican
        self.probDemocrat = probDemocrat
    
    def Borda(self):
        pass

    def Ranked(self):
        pass

    def Plurality(self):
        vote = random.randint(0, 100)
        republican = self.probRepublican * 100
        democrat = self.probDemocrat * 100 + republican
        if vote <= republican:
            return "Republican"
        elif republican < vote and vote <= democrat:
            return "Democrat"
        else:
            return "Independent"
        