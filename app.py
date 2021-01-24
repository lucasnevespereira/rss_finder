from flask import Flask, render_template, request
from scripts import rss_finder as finder
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/result", methods=["POST"])
def result():
    term = request.form["search"]
    index = request.form["page"]
    data = finder.init_finder(term, int(index))
    results_count = str(len(data))
    if len(data) == 0:
        data = ""
        results_count = "0"
    return render_template("result.html", results=data, num_results=results_count)


if __name__ == "__main__":
    app.run(debug=True)
