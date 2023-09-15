from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)

def connect_db():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="password",
        database="test"
    )
    return connection

def get_rows():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT name, age FROM users")
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows

@app.route("/")
def index():
    rows = get_rows()
    return render_template("index.html", rows=rows)

@app.route("/input", methods=["POST"])
def input():
    name = request.form["name"]
    age = request.form["age"]
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", (name, age))
    connection.commit()
    cursor.close()
    connection.close()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
