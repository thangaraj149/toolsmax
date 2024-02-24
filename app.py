from flask import Flask, render_template, request, redirect, session
import secrets
app = Flask(__name__)

# Route for the home  page
@app.route('/')
def home():
    return render_template("intex.html")




if __name__ == '__main__':
    app.run(debug=True)
