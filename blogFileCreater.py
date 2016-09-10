import tripAdvisorScraper
import csv

"""
This file creates the csv file for the randomized restaurent picking
The city being scraped is specified in tripAdvisorScraper.py
"""



def makeNewCSVOfRestaurents():
    """
    Makes a file named restaurentsVisited.csv that contains a list of lists
    in the following format:
    Number, Name, URL, Visited, Rating
    By default, numbers start at 1 and Visited is markd as no
    """
    restaurents = tripAdvisorScraper.getAllCityEateryNames()
    f = open('restaurentsVisited.csv', 'w')
    f.write("Number, Restaurent Name, Trip Advisor URL, Visited?, Rating\n")
    i = 1
    for rest in restaurents:
        f.write(str(i) +",")
        i = i + 1
        f.write(str(rest[0]) + ',')
        f.write(str(rest[1]) + ',')
        f.write("no,")
        f.write("\n")



if __name__ == "__main__":
    makeNewCSVOfRestaurents()
