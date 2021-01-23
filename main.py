from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html",)


@app.route("/result", methods=["POST"])
def result():
    term = request.form["search"]
    return render_template("result.html", results=term)


if __name__ == "__main__":
    app.run(debug=True)
