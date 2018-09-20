# Theodore Peters
# SoftDev1 pd7
# K8 -- Fill Yer Flask
# 2018-09-20

from flask import Flask

app = Flask(__name__)

@app.route("/")
def a():
    return "<h1>if this photo was a yeet, you could hit it to do things.</h1><br/><a href='/fridayInRoom413'><img src='https://cdn.discordapp.com/attachments/484851281983438851/484853232364158996/headsinhadn.png'/></a>"

@app.route("/fridayInRoom413")
def b():
    return "<a href='/ifthisiswinningiwishihadlost'><img src = 'https://cdn.discordapp.com/attachments/484851281983438851/484855255574642700/gmodification.png'/></a>"

@app.route("/ifthisiswinningiwishihadlost")
def c():
    return "<a href='/'><img src = 'https://cdn.discordapp.com/attachments/484851281983438851/484852837117853698/chemtrails.png'/></a>"

if __name__ == "__main__":
    app.debug = True
    app.run()
