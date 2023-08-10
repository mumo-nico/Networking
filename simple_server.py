import http.server
import socketserver
from utils.get_address import *
from utils.random_port import *


# Define the request handler
class SimpleHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    pass

# Set up the server
# print(get_local_ip())
IP_ADDRESS = get_local_ip()  # Takes laptop's IP address dynamically
PORT = random_port()  # Takes a random port number

server_address = (IP_ADDRESS, PORT)
httpd = socketserver.TCPServer(server_address, SimpleHTTPRequestHandler)

print(f"Serving at {IP_ADDRESS}:{PORT}")
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\nServer stopped.")