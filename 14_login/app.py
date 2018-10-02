from flask import Flask, session, render_template, request
from os import urandom
app = Flask(__name__)

users = {"Sheldon", "bazinga"}

@app.route("/")
def login():
    getKey()
    return "hello"


def getKey():
    print("a")
    try:
        p = open("data/secret.txt", "r")
        fl = p.readlines()
        app.secret_key = f1[0][:32]
        p.close()
    except FileNotFoundError:
        p = open("data/secret.txt", "w")
        app.secret_key = urandom(32)
        p.write(app.secret_key)
        p.close()
    print(app.secret_key)
if __name__ == "__main__":
    app.debug = True
    app.run()
