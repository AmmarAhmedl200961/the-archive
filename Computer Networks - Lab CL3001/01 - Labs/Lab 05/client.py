import socket

# Server details
SERVER_IP = "127.0.0.1"
SERVER_PORT = 5006

# Create UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Get user input
message = input("Enter Message: ")

# Send message to server
client_socket.sendto(message.encode(), (SERVER_IP, SERVER_PORT))

# Receive response from server
response, _ = client_socket.recvfrom(2048)
print("Server Message:", response.decode())

# Close socket
client_socket.close()


