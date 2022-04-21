import random

class Newspaper():
    def __init__(self, affiliation, influence = "Generate"):
        self.affiliation = affiliation
        if (influence == "Generate"):
            self.influence = influence 
        else:
            self.influence = random.randint(0, 8)

    # Newspapers could influence up to 8%, from 
    def swayVoter(self, voter):
        
