# Importing the Flask module
from flask import Flask, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculate", methods=['GET', 'POST'])
def calculating_tax():
    return render_template("calculate.html")

@app.route("/exporting", methods=['GET', 'POST'])
def exporting_spreadsheet():
    return render_template("exporting.html")
# Want to create an Excel/CSV export of the data

if __name__ == "__main__":
    app.run(debug=False)