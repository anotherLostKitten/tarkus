# Didactic Katydids -- Theodore Peters, Raymond Wu
# SoftDev1 pd7
# K06 -- Stl/O: Divine your Destiny!
# 2018-09-14

from os import getcwd
from os.path import isfile

def getPath(prompt):
    while True:
        path = getcwd() + "/" + input(prompt)
        print(path)
        if isfile(path):
            return path

def cvsToDict(workingDict):
    f = open(getPath("File name (occupations.csv, perhaps?) << "), 'r')
    lines = f.readlines()
    total = 0
    for i in lines[1 : ]:
        comma = i.rfind(",")
        if i[ : comma] == "Total":
            total = float(i[comma + 1 : -1])
        elif i[0] == "\"":
            workingDict[i[1 : comma - 1]] = float(i[comma + 1 : -1])
        else:
            workingDict[i[ : comma]] = float(i[comma + 1 : -1])
    f.close()
    return total

d = dict()
cvsToDict(d)
print(d)
    
    
    
