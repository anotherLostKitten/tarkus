# Theodore Peters
# SoftDev1 pd7
# K24 -- i remebered to do a heading this time i'm a reformed fella
# 2018-11-13

from flask import Flask, render_template

import urllib, json
app = Flask(__name__)

@app.route("/")
def a():
    u = urllib.request.urlopen("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&date=2007-04-24")
    response = u.read()
    print(response)
    data = json.loads(response)
    print(data)
    return render_template("bazinga.html", earl=data["url"], desk=data["explanation"])

if __name__ == "__main__":
    app.debug = True
    app.run()
