import os
import time
import spacy
from flask import Flask, jsonify, Response, request, send_from_directory, render_template, send_file
from apiflask import APIFlask, Schema
from flask_cors import CORS
from apiflask.fields import Integer, String, Boolean, List, Nested, Date, Float
import os
import subprocess
import utils
import global_alignment as global_alignment
import local_alignment as local_alignment
import fitting_alignment as fitting_alignment
import utils as utils
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import seaborn as sns

THRESHOLD_VALS = 500

import matplotlib.pyplot as plt

class RetVals(Schema):
    local_align = String()
    global_align = String()
    fitting_align = String()  

    local_score = Integer()
    global_score = Integer()
    fitting_score = Integer()

class Inputs(Schema):
    text1 = String()
    text2 = String()

nlp = spacy.load("en_core_web_sm")

# Initialize the API
app = APIFlask(
    __name__,
    title="PokerChipCounter",
    static_url_path="/static",
    static_folder="./static")

CORS(app, resources={r"/*": {"origins": "*"}})

IMAGE_FOLDER = 'API/images/'

@app.route('/local_image')
def get_image_local():
    return send_file("static/local_align.png", mimetype="image/png")

@app.route('/fitting_image')
def get_image_fitting():
    return send_file("static/fitting_align.png", mimetype="image/png")

@app.route('/global_image')
def get_image_global():
    return send_file("static/global_align.png", mimetype="image/png")

@app.route('/submit', methods = ['POST'])
@app.input(Inputs, location="json")
@app.output(RetVals)
def aa(json_data):
    text = json_data['text1']
    text2 = json_data['text2']

    doc = nlp(text)
    doc2 = nlp(text2)


    a = utils.doc_to_characters(doc)
    b = utils.doc_to_characters(doc2)

    g = global_alignment.GlobalAlignment()
    l = local_alignment.LocalAlignment()
    f = fitting_alignment.FittingAlignment()

    x, y, mg, gve, gwe = g.align(a, b)
    v, w, ml, lve, lwe = l.align(a, b)
    t, u, mf, fve, fwe = f.align(a, b)

    plt.figure(figsize=(10, 8))

    cur = (mg, gve, gwe, "Global Alignment DP Matrix")
    if len(cur[0]) * len(cur[0][0]) < THRESHOLD_VALS:
        sns.heatmap(cur[0], annot=True, fmt="d", cmap="Blues", xticklabels=list(cur[2]), yticklabels=list(cur[1]))
    else:
        sns.heatmap(cur[0], annot=False, cmap="Blues", xticklabels=list(cur[2]), yticklabels=list(cur[1]))

    plt.title(cur[3])
    plt.xlabel("Sequence 2")
    plt.ylabel("Sequence 1")
    plt.savefig("API/static/global_align.png")
    plt.clf()

    cur = (mf, fve, fwe, "Fitting Alignment DP Matrix")
    if len(cur[0]) * len(cur[0][0]) < THRESHOLD_VALS:
        sns.heatmap(cur[0], annot=True, fmt="d", cmap="Blues", xticklabels=list(cur[2]), yticklabels=list(cur[1]))
    else:
        sns.heatmap(cur[0], annot=False, cmap="Blues", xticklabels=list(cur[2]), yticklabels=list(cur[1]))

    plt.title(cur[3])
    plt.xlabel("Sequence 2")
    plt.ylabel("Sequence 1")
    plt.savefig("API/static/fitting_align.png")
    plt.clf()

    cur = (ml, lve, lwe, "Local Alignment DP Matrix")
    if len(cur[0]) * len(cur[0][0]) < THRESHOLD_VALS:
        sns.heatmap(cur[0], annot=True, fmt="d", cmap="Blues", xticklabels=list(cur[2]), yticklabels=list(cur[1]))
    else:
        sns.heatmap(cur[0], annot=False, cmap="Blues", xticklabels=list(cur[2]), yticklabels=list(cur[1]))

    plt.title(cur[3])
    plt.xlabel("Sequence 2")
    plt.ylabel("Sequence 1")
    plt.savefig("API/static/local_align.png")
    plt.clf()

    a = {'local_align': u, 'local_score': int(t), 'global_align': y, 'global_score': int(x), 'fitting_align': w, 'fitting_score': int(v)}

    return jsonify(a), 200



if __name__ == "__main__":
    port = int(os.environ.get('PORT', 443))
    # connected = False

    # while not connected:
    #     try:
    #         start_db()
    #         connected = True
    #     except database.psycopg2.OperationalError as e:
    #         print("Could not connect to database")

    #     time.sleep(2)

    app.run(debug=True, host="0.0.0.0", port=port, use_reloader=True)
