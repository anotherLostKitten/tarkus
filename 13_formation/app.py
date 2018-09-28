from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def template():
    return render_template("/a.html")

@app.route("/auth", methods = ["GET"])
def isBazina():
    print(request.method)
    return render_template("/b.html", a = request.args['bazinga'])
@app.route("/auth", methods = ["POST"])
def isBazinga():
    print(request.method)
    return render_template("/b.html", a = request.form['bazinga'])
if __name__ == "__main__":
    app.debug = True
    app.run()
