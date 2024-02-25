from flask import Flask, render_template, request, redirect, session
import secrets
app = Flask(__name__)

# Route for the home  page
@app.route('/')
def home():
    return render_template("intex.html")

@app.route('/')
def home():
    return render_template("about.html")

@app.route('/')
def home():
    return render_template("aerators.html")
    
@app.route('/')
def home():
    return render_template("blowers.html")

@app.route('/')
def home():
    return render_template("carpet.html")

@app.route('/')
def home():
    return render_template("compactors.html")

@app.route('/')
def home():
    return render_template("concrete.html")

@app.route('/')
def home():
    return render_template("contact.html")

@app.route('/')
def home():
    return render_template("coredrill.html")

@app.route('/')
def home():
    return render_template("dc.html")

@app.route('/')
def home():
    return render_template("demolition.html")

@app.route('/')
def home():
    return render_template("drain.html")

@app.route('/')
def home():
    return render_template("drainclean.html")

@app.route('/')
def home():
    return render_template("floor.html")

@app.route('/')
def home():
    return render_template("flr.html")

@app.route('/')
def home():
    return render_template("grinder.html")

@app.route('/')
def home():
    return render_template("largerent.html")

@app.route('/')
def home():
    return render_template("login.html")

@app.route('/')
def home():
    return render_template("paint.html")

@app.route('/')
def home():
    return render_template("paints.html")

@app.route('/')
def home():
    return render_template("pressure.html")

@app.route('/')
def home():
    return render_template("rent.html")

@app.route('/')
def home():
    return render_template("rentform.html")

@app.route('/')
def home():
    return render_template("sales.html")

@app.route('/')
def home():
    return render_template("signup.html")
     
if __name__ == '__main__':
    app.run(debug=True)
