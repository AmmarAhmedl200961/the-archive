import socket

def start_client(client_id):
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Define the host and port of the server
    host = '127.0.0.1'  # Localhost
    port = 8000
    
    # Connect to the server
    client_socket.connect((host, port))
    
    # Send a message to the server
    message = f"Hello I am client and My id is {client_id}"
    client_socket.send(message.encode('utf-8'))
    
    # Receive the response from the server
    response = client_socket.recv(1024).decode('utf-8')
    print(f"Server response: {response}")
    
    # Close the client socket
    client_socket.close()

if __name__ == "__main__":
    client_id = input("Enter client ID (0-9): ")
    if client_id.isdigit() and 0 <= int(client_id) <= 9:
        start_client(client_id)
    else:
        print("Invalid client ID. Please enter a single digit from 0 to 9.")

