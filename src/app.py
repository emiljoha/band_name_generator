import os
from flask import Flask, jsonify, send_from_directory, render_template
from flask_cors import CORS
from band_name_generator import get_new_album

app = Flask(__name__)
CORS(app)


@app.route('/')
def root():
    return render_template("index.html",
                           base_url=("http://" +
                                     os.environ['DOMAIN'] +
                                     ":" +
                                     os.environ['PORT']))


@app.route('/get_album_info', methods=['GET'])
def get_album_info():
    return jsonify(get_new_album())


@app.route('/albums/<path:path>')
def send_js(path):
    return send_from_directory('albums', path)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ['PORT'])
