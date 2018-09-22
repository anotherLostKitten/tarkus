# Theodore Peters, Jason Lin -- Name of Team's Team Name
# SoftDev1 pd7
# K10 -- Jinja Tuning
# 2018-09-24

from flask import Flask, render_template
from os import getcwd
from random import random
from csv import reader


app = Flask(__name__)

@app.route("/")
def hello_world():
    print(__name__ + "\n")
    return ""

@app.route("/my_foist_template")
def template():
    d = csvToDict()
    t = round(sum(d.values()), 1)
    r = weightedRandom(d, t)
    return render_template("/a.html", jobDict = d, result = r, total = t)

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

if __name__ == "__main__":
    app.debug = True
    app.run()
