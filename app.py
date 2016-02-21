from flask import Flask
from utils.bullshit_util import  get_bullshit_count
import csv
import sys

app = Flask(__name__)

bullshit_list_csv = sys.argv[1]
bullshit_candidate_text = sys.argv[2]

bullshit_list = {}

@app.route("/score")
def bullshit_score():
    x = 1

if __name__ == '__main__':
    with open(bullshit_list_csv) as f:
        reader = csv.reader(f)
        for row in reader:
            bullshit_list[row[0]] = row[1]
    print(bullshit_list)
    with open (bullshit_candidate_text, "r") as bsf:
        data = bsf.readlines()
    print(data[0])
    results = get_bullshit_count(data[0], bullshit_list)
    print(results)

