from flask import Flask, render_template, request, redirect, session
import secrets
app = Flask(__name__)

# Route for the home  page
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/aerators')
def aerators():
    return render_template("aerators.html")
    
@app.route('/blowers')
def blowers():
    return render_template("blowers.html")

@app.route('/carpet')
def carpet():
    return render_template("carpet.html")

@app.route('/compactors')
def compactors():
    return render_template("compactors.html")

@app.route('/concrete')
def concrete():
    return render_template("concrete.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/coredrill')
def coredrill():
    return render_template("coredrill.html")

@app.route('/dc')
def dc():
    return render_template("dc.html")

@app.route('/demolitions')
def demolition():
    return render_template("demolition.html")

@app.route('/drain')
def drain():
    return render_template("drain.html")

@app.route('/drainclean')
def drainclean():
    return render_template("drainclean.html")

@app.route('/floor')
def floor():
    return render_template("floor.html")

@app.route('/flr')
def flr():
    return render_template("flr.html")

@app.route('/grinder')
def grinder():
    return render_template("grinder.html")

@app.route('/largerent')
def largerent():
    return render_template("largerent.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/paint')
def paint():
    return render_template("paint.html")

@app.route('/paints')
def paints():
    return render_template("paints.html")

@app.route('/pressure')
def pressure():
    return render_template("pressure.html")

@app.route('/rent')
def rent():
    return render_template("rent.html")

@app.route('/rentform')
def rentform():
    return render_template("rentform.html")

@app.route('/rentacc')
def rentacc():
    return render_template("rentacc.html")

@app.route('/sales')
def sales():
    return render_template("sales.html")

@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route('/truck')
def truck():
    return render_template("truck.html")

     
if __name__ == '__main__':
    app.run(debug=True)
