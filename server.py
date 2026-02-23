from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/dashboard')
def dashboard():
    return jsonify({
        "revenue": {"monthly_current": 3500, "monthly_target": 16667},
        "agents": 6
    })

@app.route('/api/agents')
def agents():
    return jsonify({"agents": [
        {"name": "CEO Agent", "status": "online"},
        {"name": "CMO Agent", "status": "online"}
    ]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
