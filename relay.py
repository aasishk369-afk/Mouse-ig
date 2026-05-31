from flask import Flask, request, jsonify

app = Flask(__name__)
# This list holds the commands until the agent is ready for them
command_queue = []

# This is where your Discord Bot sends commands
@app.route('/send_command', methods=['POST'])
def send_command():
    data = request.json
    command_queue.append(data['command'])
    return jsonify({"status": "command_received"}), 200

# This is where your Agent asks for new instructions
@app.route('/get_command', methods=['GET'])
def get_command():
    if command_queue:
        return jsonify({"command": command_queue.pop(0)}), 200
    return jsonify({"command": "none"}), 200

if __name__ == '__main__':
    # Railway will provide the PORT automatically
    app.run(host='0.0.0.0', port=5000)
