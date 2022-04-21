from Voter import Voter
from Newspaper import Newspaper

class County():
  def __init__(self, name, population, newspapers, affiliation, percentRepublican, percentDemocrat):
    self.population = population
    self.name = name
    self.percentRepublican = percentRepublican
    self.percentDemocrat = percentDemocrat
    self.voters = []
    self.newpapers = []
    for i in range(self.population):
      self.voters.append(Voter(self.percentRepublican, self.percentDemocrat))
    for i in range(newspapers):
      self.newpapers.append(0)
  # How do we want to set for each voting method
  # since we will want to run all 3 each time or do 
  # we want each sim to run only one at a time?
  def countyVotePlurality(self):
    votes = {"Republican": 0, "Democrat": 0, "Independent": 0}
    # For each voter, call the plurality function to get the vote and increment
    for voter in self.voters:
      vote = voter.Plurality()
      votes.vote += 1
    return votes

  def countyVoteBorda(self):
    votes = {"Republican": 0, "Democrat": 0, "Independent": 0}
    for voter in self.voters:
      vote = voter.Borda()
      votes.vote += 1
    return votes

  def countyVoteRanked(self):
    votes = {"Republican": 0, "Democrat": 0, "Independent": 0}
    for voter in self.voters:
      vote = voter.Ranked()
      votes.vote += 1
    return votes

