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
