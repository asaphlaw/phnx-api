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
@app.route('/api/activity')
def activity():
    return jsonify({
        "activities": [
            {"agent": "CEO Agent", "action": "Generated morning brief", "details": "Revenue gap identified", "timestamp": "2026-02-23T06:00:00"},
            {"agent": "CMO Agent", "action": "Published marketing brief", "details": "Content velocity priority", "timestamp": "2026-02-23T06:30:00"},
            {"agent": "Calendar Sync", "action": "Completed sync", "details": "5 sessions processed", "timestamp": "2026-02-23T21:00:00"}
        ]
    })
