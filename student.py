from flask import Flask, url_for, redirect, render_template, request
import sqlite3 as sql
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def home():
    return render_template("home.htm")

@app.route("/enternew")
def new_student():
    return render_template("student.htm")

@app.route("/addrec", methods = ["POST", "GET"])
def addrec():
    if request.method == "POST":
        nm = request.form["nm"]
        addr = request.form["addr"]
        city = request.form["city"]
        zip = request.form["zip"]

        cmd = "INSERT INTO students (name, addr, city , zip) VALUES ('{0}', '{1}', '{2}', '{3}')".format(nm, addr, city, zip)

        with sql.connect("database.db") as conn:
            cur = conn.cursor()
            cur.execute(cmd)
            conn.commit()
            msg = "Student data successfully saved."
            return render_template("output.htm", msg = msg)

@app.route("/list")
def list():
    conn = sql.connect("database.db")
    conn.row_factory = sql.Row

    cmd = "SELECT * FROM students"
    cur = conn.cursor()
    cur.execute(cmd)
    rows = cur.fetchall()
    conn.close()
    return render_template("list.htm", rows = rows)


if __name__ == "__main__":
    app.run(debug = True)

