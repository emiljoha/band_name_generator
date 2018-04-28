from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from band_name_generator import get_new_album
from config.secret_config import port

app = Flask(__name__)
CORS(app)


@app.route('/get_album_info', methods=['GET'])
def get_album_info():
    return jsonify(get_new_album())


@app.route('/albums/<path:path>')
def send_js(path):
    return send_from_directory('albums', path)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
