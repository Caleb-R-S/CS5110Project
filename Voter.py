import random

class Voter():
    def __init__(self, probRepublican, probDemocrat) :
        self.probRepublican = probRepublican
        self.probDemocrat = probDemocrat
    
    def Borda(self):
        probIndependant = 1 - self.probRepublican - self.probDemocrat
        vote = random.randint(0, 100)
        pass

    def Ranked(self):
        probIndependant = 1 - self.probRepublican - self.probDemocrat
        vote = random.randint(0, 100)
        if(vote <= self.probRepublican * 100):
            return "Republican"
        elif(self.probRepublican and vote <= self.probDemocrat and vote < probIndependant):
            return "Democrat"
        else:
            return "Independent"

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
        
testVoter = Voter(0.5, 0.5)
print(testVoter.Ranked())