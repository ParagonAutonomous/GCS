from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/status/', methods=['GET'])
def status():
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)