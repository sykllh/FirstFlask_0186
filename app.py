
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", nama=None, nim=None)

@app.route("/submit", methods=["POST"])
def submit():
    nama = None
    nim = None

    nama = request.form.get("nama")
    if not nama:
        nama = "Anonim"

    nim = request.form.get("nim")
    if not nim:
        nim = "-"

    return render_template("index.html", nama=nama, nim=nim)

if __name__ == "__main__":
    app.run(debug=True)