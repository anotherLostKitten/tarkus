# Theodore Peters
# SoftDev1 pd7
# K26 -- a b c d e f g h i j k l m n o p q r s t u v w x y z
# 2018-11-16

from flask import Flask, render_template

import urllib, json
app = Flask(__name__)

@app.route("/")
def a():
    u = urllib.request.urlopen("https://api.icndb.com/jokes/random")
    response = u.read()
    #print(response)
    data = json.loads(response)
    #print(data)
    u.close()
    
    u = urllib.request.urlopen("https://dog.ceo/api/breed/dachshund/images/random")
    response = u.read()
    data1 = json.loads(response)
    
    
    u = urllib.request.urlopen("http://numbersapi.com/42/trivia")
    data2 = u.read().decode('utf8')
    print(data2)
    return render_template("bazinga.html", desk=data["value"]["joke"], earl1=data1["message"], desk2=str(data2))

if __name__ == "__main__":
    app.debug = True
    app.run()
