import os
import time

from flask import Flask, jsonify, Response, request, send_from_directory, render_template
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
    return render_template("local_render.html")

@app.route('/fitting_image')
def get_image_fitting():
    return send_from_directory(IMAGE_FOLDER, "fitting_align.ng")

@app.route('/global_image')
def get_image_global():
    return send_from_directory(IMAGE_FOLDER, "global_align.png")

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
