import random

class Newspaper():
    def __init__(self, affiliation, influence = "Generate"):
        self.affiliation = affiliation
        if (influence == "Generate"):
            # Newspapers could influence up to 8%, from 
            influence = random.randint(0, 8) / 100
        self.influence = abs(affiliation * influence)

    def swayVoter(self, voter):
        if self.affiliation < 0:
            voter.setPropRepublican(voter.getProbRepublican() + self.influence)
            voter.setProbDemocrat(voter.getProbDemocrat() - self.influence)
        else:
            voter.setPropRepublican(voter.getProbRepublican() - self.influence)
            voter.setProbDemocrat(voter.getProbDemocrat() + self.influence)

