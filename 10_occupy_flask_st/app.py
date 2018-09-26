# Theodore Peters, Jason Lin -- CuriousIncident
# SoftDev1 pd7
# K10 -- Jinja Tuning
# 2018-09-24

from flask import Flask, render_template
from util import occupation

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Do you want to look at <a href='/occupations'>job?</a>"

@app.route("/occupations")
def template():
    jobDict = occupation.csvToDict()
    total = round(sum(jobDict.values()), 1)
    result = occupation.weightedRandom(jobDict, total)
    return render_template("/a.html", jobDict = jobDict, result = result, total = total)

if __name__ == "__main__":
    app.debug = True
    app.run()
