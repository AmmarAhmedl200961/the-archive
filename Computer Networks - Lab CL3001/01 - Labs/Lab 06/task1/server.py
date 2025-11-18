import socket

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Define the host and port
    host = '127.0.0.1'  # Localhost
    port = 8000
    
    # Bind the socket to the host and port
    server_socket.bind((host, port))
    
    # Listen for incoming connections
    server_socket.listen(5)  # Allow up to 5 pending connections
    
    print(f"Server listening on {host}:{port}")
    
    while True:
        # Accept a new connection
        client_socket, address = server_socket.accept()
        print(f"Connection from {address}")
        
        # Receive data from the client
        data = client_socket.recv(1024).decode('utf-8')
        print(f"Received from client: {data}")
        
        # Extract the client ID from the message
        client_id = data.split("My id is ")[1].split(".")[0]
        
        # Send a response back to the client
        response = f"Hello I am server. Your received id is {client_id}"
        client_socket.send(response.encode('utf-8'))
        
        # Close the client socket
        client_socket.close()

if __name__ == "__main__":
    start_server()

