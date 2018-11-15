# Theodore Peters
# SoftDev1 pd7
# K24 -- i remebered to do a heading this time i'm a reformed fella
# 2018-11-13

from flask import Flask, render_template

import urllib, json
app = Flask(__name__)

@app.route("/")
def a():
    u = urllib.request.urlopen("http://xkcd.com/1481/info.0.json")
    response = u.read()
    print(response)
    data = json.loads(response)
    print(data)
    return render_template("bazinga.html", earl=data["img"], desk=data["alt"])

if __name__ == "__main__":
    app.debug = True
    app.run()
