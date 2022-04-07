# -*- coding: utf-8 -*-
import sys, os
import Arizona
from County import County
def main():
    nameOfSimulation = input("Please Enter Name Of The Simulation: ")
    counties  = readCSV(os.getcwd() + '/Data/Simulations/' + nameOfSimulation)
    for county in counties:
        final = f"""
County Name: {county.name}
County Population: {county.population}
        """
        print(final)

def readCSV(fileName):
    file = open(fileName)
    counties = []
    file.readline()
    for line in file:
        split = line.split(",")
        # name, population, newspapers, affiliation, percentR, percentD
        counties.append(County(split[0], int(split[6]), int(split[1]), float(split[2]), float(split[3]), float(split[4])))
    file.close()

    return counties

def simulation(fileName):
    counties = readCSV(fileName)
    az = Arizona(counties)


main()