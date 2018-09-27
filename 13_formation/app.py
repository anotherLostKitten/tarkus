from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def template():
    print(app)
    return render_template("/a.html")

@app.route("/auth")
def isBazina():
    return render_template("/b.html", a = request.args['bazinga'])

if __name__ == "__main__":
    app.debug = True
    app.run()
