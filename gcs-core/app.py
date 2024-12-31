from flask import Flask, jsonify
from app import create_app

app = create_app()

@app.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)