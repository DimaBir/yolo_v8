from flask import Flask, jsonify
import test_preprocess
import config

app = Flask(__name__)


@app.route('/run-tests', methods=['GET'])
def run_tests():
    try:
        test_preprocess.test_data_preprocessing_service("http://data-preprocessing-service:5000")
        return jsonify({"status": "success", "message": "Tests passed."}), 200
    except AssertionError as e:
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=config.FLASK_DEBUG, host=config.FLASK_HOST, port=config.FLASK_PORT)