# Didactic Katydids -- Theodore Peters, Raymond Wu
# SoftDev1 pd7
# K06 -- Stl/O: Divine your Destiny!
# 2018-09-14

from os import getcwd
from os.path import isfile
from random import random
from csv import reader

# Repeatedly prompts user for a file from working directory until they select a valid file.
#   prompt specifies prompt text.
def getPath(prompt, defaultPath):
    while True:
        userin = input(prompt)
        path = getcwd() + "/" + userin
        if userin == "":
            return path + defaultPath
        if isfile(path):
            return path
        print("File not found. Try again.\n")

# Reads occupations.csv, returns a dictionary with occupation-string keys and weighted-floating-point values
def csvToDict():
    # prepare an occupations dictionary to be returned...
    occupations = {}

    # open the csv file object, bind to variable
    csvFileObject = open(getPath("Choose file name. Leave blank for occupations.csv. | ", "occupations.csv"), 'r')
    # read the records in the csv
    readerObject = reader(csvFileObject)
    
    for record in readerObject:
        # skip over the first & last records
        if record[0] == "Job Class" or record[0] == "Total":
            continue
        # record[0] is the occupation string, record[1] is the floating point (as a string)
        # must convert appropriate string into floating point before placing as value in dict
        else:
            occupations[ record[0] ] = float(record[1])
            
    csvFileObject.close()
    return occupations

# Picks a random dict value based on the weigts given in a dict of strings to their weights.
def weightedRandom(wc, total = None):
    if total == None: # If the total of the weights is known, can avoid calculating sum
        total = sum(wc.values()) # Possibly useful if finding weighted random several times.
    endWeight= total * random() # endWeight in correct range when curWeight >= endWeight
    curWeight = 0
    for i in wc:
        curWeight += wc[i]
        if curWeight >= endWeight:
            return i # dict value.
    raise ValueError("Value of total passed was incorrect.") # If the function gets here,
                                                             # user pased a total value that
                                                             # was wrong.



d = csvToDict()
print(weightedRandom(d))

    
