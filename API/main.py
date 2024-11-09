import os
import time

from flask import Flask, jsonify, Response, request, send_from_directory, render_template, send_file
from apiflask import APIFlask, Schema
from flask_cors import CORS
from apiflask.fields import Integer, String, Boolean, List, Nested, Date, Float
import os
import subprocess

import matplotlib.pyplot as plt

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

@app.route('/aa')
def aa():
    return os.listdir('.')


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
