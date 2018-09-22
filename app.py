from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    print(__name__ + "\n")
    return ""

@app.route("/my_foist_template")
def template():
    return render_template("/a.html", src = "harold.jpg", coll = fib(5000))

def fib(n):
    a = [0,1]
    while len(a) < n:
        a.append(a[-1] + a[-2])
    return a
if __name__ == "__main__":
    app.debug = True
    app.run()
