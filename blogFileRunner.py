import random


BLOG_FILENAME = 'restaurentsVisited.csv'



def readInBlogFile():
    """
    Reads in the csv in BLOG_FILENAME and returns as a list of lists
    """
    f = open(BLOG_FILENAME, 'r')
    restaurents = []
    for line in f:
        line = line.split(',')
        restaurents.append(line)
    f.close()
    return restaurents

def chooseRandomUnvisited(restaurents):
    """
    Returns a random unvisited restaurent number
    The number is one offset from the index in restaurents
    """
    unvisitedRestNumbers = []
    for rest in restaurents:
        if rest[3] == 'no':
            unvisitedRestNumbers.append(int(rest[0]))
    choice = random.choice(unvisitedRestNumbers)
    return choice
    
def printChoice(choiceNum, restaurents):
    """
    Prints the name and URL of the restaurent choiceNum
    """
    print "The restaurent you chose was: ",
    print restaurents[choiceNum - 1][1]
    print "Url: ",
    print restaurents[choiceNum - 1][2]
    return raw_input("Do you want to go there, yes or no?  ")



def markUnvisitedAsVisited(choiceNum, restaurents):
    """
    Marks the restaurent with id choiceNum as visited
    """
    restaurents[choiceNum - 1][3] = "yes"
    return restaurents

def printBlogFile(restaurents):
    """
    Writes the list in restaurents to the file named BLOG_FILENAME
    """
    f = open(BLOG_FILENAME, 'w')
    for rest in restaurents:
        for i in range(len(rest)):
            if i < (len(rest) - 1):
                f.write(rest[i] + ',')
            else:
                f.write(rest[i])

if __name__=="__main__":
    """
    This main allows the user to choose a restaurent and save that they've
    visited
    """
    restaurents = readInBlogFile()
    nextChoice = chooseRandomUnvisited(restaurents)
    answer = printChoice(nextChoice, restaurents)
    if answer == "yes":
        restaurents = markUnvisitedAsVisited(nextChoice, restaurents)
        print restaurents[nextChoice - 1]
        printBlogFile(restaurents)
        print "Thank you, have fun!"
    else:
        print "That's ok for now!"




