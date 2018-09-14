# Didactic Katydids -- Theodore Peters, Raymond Wu
# SoftDev1 pd7
# K06 -- Stl/O: Divine your Destiny!
# 2018-09-14

from os import getcwd
from os.path import isfile
from random import random

# Repeatedly prompts user for a file from working directory until they select a valid file.
#   prompt specifies prompt text.
def getPath(prompt):
    while True:
        path = getcwd() + "/" + input(prompt)
        if isfile(path):
            return path
        print("File not found. Try again.\n")

# Formats a user chosen file to a dictionary that maps
# strings to float values representing weights.
# workingDict modified by function, returns sum of weigts.
def cvsToDict(workingDict):
    f = open(getPath("File name (occupations.csv, perhaps?) << "), 'r')
    lines = f.readlines()
    total = 0
    for i in lines[1 : ]: # skipping first line, which is header
        comma = i.rfind(",")
        if i[ : comma] != "Total": # total percent should not be in dict
            # vv   adds a item : percent chance key/val pair to given dict
            workingDict[i[ : comma].replace("\"", "")] = float(i[comma + 1 : -1])
            total += float(i[comma + 1 : -1])
    f.close()
    return total # return total value to make calculation of weighted random easier

# Picks a random number based on the weigts given in a dict of strings to their weights.
def weightedRandom(wc, total = None):
    if total == None: # If the total of the weights is known, can avoid calculating sum
        total = sum(wc.values()) # Possibly useful if finding weighted random several times.
    endWeight= total * random() # endWeight in correct range when curWeight >= endWeight
    curWeight = 0
    for i in wc:
        curWeight += wc[i]
        if curWeight >= endWeight:
            return i
    raise ValueError("Value of total passed was incorrect.") # If the function gets here,
                                                             # user pased a total value that
                                                             # was wrong.



d = dict()
cvsToDict(d)
print(d)

    
