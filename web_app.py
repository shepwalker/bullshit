from flask import Flask, request, render_template
from utils.bullshit_util import  get_bullshit_count
import csv
import sys

app = Flask(__name__)
app.config['DEBUG'] = True

bullshit_list_csv = sys.argv[1]
bullshit_candidate_text = sys.argv[2]

bullshit_list = {}

with open(bullshit_list_csv) as f:
        reader = csv.reader(f)
        for row in reader:
            bullshit_list[row[0]] = row[1]



@app.route("/score", methods=["GET", "POST"])
def bullshit_score():
    if request.method == 'POST':
        text = request.values.get("text", '')
        results = get_bullshit_count(text, bullshit_list)
    text = request.values.get("text", '')
    results = get_bullshit_count(text, bullshit_list)
    return results


@app.route("/jstest", methods=["GET"])
def jstest():
    return render_template("test.html")

if __name__ == '__main__':
    app.run()