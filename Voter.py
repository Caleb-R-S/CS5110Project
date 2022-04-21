import random

class Voter():
    def __init__(self, probRepublican, probDemocrat) :
        self.probRepublican = probRepublican
        self.probDemocrat = probDemocrat
    
    def setProbRepublican(self, newProb):
        self.probRepublican = newProb
    
    def setProbDemocrat(self, newProb):
        self.probDemocrat = newProb

    def getProbRepublican(self):
        return self.probRepublican 
 
    def getProbDemocrat(self):
        return self.probDemocrat
    
    def Borda(self):
        probIndependant = 1 - self.probRepublican - self.probDemocrat
        vote = random.randint(0, 100)
        pass

    def Ranked(self):
        probIndependant = 1 - self.probRepublican - self.probDemocrat
        print(self.probRepublican)
        print(self.probDemocrat)
        print(probIndependant)

        vote = ()

        vote = random.randint(0, 100)
        if(vote <= self.probRepublican * 100):
            
            vote.append("Republican")
        elif(vote <= self.probDemocrat * 100 + self.probRepublican * 100):
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
        
testVoter = Voter(0.33, 0.33)
print(testVoter.Ranked())