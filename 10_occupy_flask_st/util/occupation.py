# this is secretly called ants

from os import getcwd
from random import random
from csv import reader

def weightedRandom(wc, total = None):
    if total == None: # If the total of the weights is known, can avoid calculating sum
        total = sum(wc.values()) # Possibly useful if finding weighted random several times.
    endWeight= total * random() # endWeight in correct range when curWeight >= endWeight
    curWeight = 0
    for i in wc:
        curWeight += wc[i]
        if curWeight >= endWeight:
            return i # dict value.
    raise ValueError("Value of total passed was incorrect.")

def csvToDict():
    # prepare an occupations dictionary to be returned...
    occupations = {}

    # open the csv file object, bind to variable
    csvFileObject = open("data/occupations.csv", 'r')
    # read the records in the csv
    readerObject = reader(csvFileObject)

    for record in readerObject:
        # skip over the first & last records
        if record[0] != "Job Class" and record[0] != "Total":
            occupations[record[0]] = float(record[1])
    csvFileObject.close()
    return occupations
