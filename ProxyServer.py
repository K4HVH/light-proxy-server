from flask import Flask, request, jsonify
import socket

app = Flask(__name__)

def send_command(ip, port, command):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ip, port))
        s.sendall(command.encode())

@app.route('/send_command', methods=['POST'])
def handle_command():
    server_ip = '10.0.0.5'
    server_port = 9999
    command = request.json.get('command', 'OFF')  # Default command
    send_command(server_ip, server_port, command)
    return jsonify(message=f"Command '{command}' sent to {server_ip}:{server_port}")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=15347)