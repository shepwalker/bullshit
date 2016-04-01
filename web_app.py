from flask import Flask, request
from utils.bullshit_util import  get_bullshit_count
import csv
import sys

app = Flask(__name__)

bullshit_list_csv = sys.argv[1]
bullshit_candidate_text = sys.argv[2]

bullshit_list = {}

with open(bullshit_list_csv) as f:
        reader = csv.reader(f)
        for row in reader:
            bullshit_list[row[0]] = row[1]

@app.route("/score", methods=["GET", "POST"])
def bullshit_score():
    text = request.values.get("text", '')
    results = get_bullshit_count(text, bullshit_list)
    return results

if __name__ == '__main__':
    app.run()