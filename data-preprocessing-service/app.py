from flask import Flask, jsonify
import logging
from preprocess import run_preprocessing
import config

app = Flask(__name__)


@app.route('/preprocess-coco', methods=['GET'])
def preprocess_coco():
    try:
        run_preprocessing()
        return jsonify({"status": "success", "message": "COCO dataset preprocessing initiated."}), 200
    except Exception as e:
        logging.error(f"Error during preprocessing: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=config.FLASK_DEBUG, host=config.FLASK_HOST, port=config.FLASK_PORT)
