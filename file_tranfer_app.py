import tkinter as tk
from tkinter import filedialog
import socket
import threading
from utils.get_address import *
from utils.random_port import *

class FileTransferApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Transfer App")

        # GUI elements
        self.source_label = tk.Label(root, text="Source IP:")
        self.source_label.pack()
        self.source_entry = tk.Entry(root)
        self.source_entry.pack()

        self.target_label = tk.Label(root, text="Target IP:")
        self.target_label.pack()
        self.target_entry = tk.Entry(root)
        self.target_entry.pack()

        self.port_label = tk.Label(root, text="Port:")
        self.port_label.pack()
        self.port_entry = tk.Entry(root)
        self.port_entry.pack()

        self.select_file_button = tk.Button(root, text="Select File", command=self.select_file)
        self.select_file_button.pack()

        self.transfer_button = tk.Button(root, text="Transfer File", command=self.transfer_file)
        self.transfer_button.pack()

        self.status_label = tk.Label(root, text="")
        self.status_label.pack()

    def select_file(self):
        # Open a file dialog to select a file
        self.file_path = filedialog.askopenfilename()

    def transfer_file(self):
        source_ip = self.source_entry.get()
        target_ip = self.target_entry.get()
        port = int(self.port_entry.get())

        try:
            with open(self.file_path, "rb") as file:
                file_data = file.read()

            target_address = (target_ip, port)

            self.status_label.config(text="Transferring...")

            def send_file():
                # Create a socket, connect to the target, and send the file
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                    sock.connect(target_address)
                    sock.sendall(file_data)

                self.status_label.config(text="File transferred successfully.")

            # Start a new thread to perform the file transfer
            threading.Thread(target=send_file).start()

        except Exception as e:
            self.status_label.config(text="Error: " + str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = FileTransferApp(root)
    root.mainloop()
