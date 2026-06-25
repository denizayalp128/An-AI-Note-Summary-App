from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    notes = ""

    if request.method == "POST":
        notes = request.form["notes"]

    return render_template("index.html", notes=notes, lenghtofnotes=len(notes))
if __name__ == "__main__":
    app.run(debug=True)
