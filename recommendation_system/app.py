from recommendation_system import get_items_to_recommend_cust
import numpy as np
import pandas as pd
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    username = request.form["uname"]
    cust_a="AVpfPjqKLJeJML435aZR"
    suggestions = get_items_to_recommend_cust(username,cust_a)
    return render_template('home.html',username = username , cust_a = cust_a,suggestions=suggestions)

@app.route("/recommend",methods=["POST","GET"])
def recommend():
    if request.method == 'POST':
        # username = request.get_json()
        username = request.form["uname"]
        cust_a="AVpfPjqKLJeJML435aZR"
        # get_user = username['user']
        suggestions = get_items_to_recommend_cust(username,cust_a)
        return "Product suggestions are: {}".format(suggestions)
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=5000)