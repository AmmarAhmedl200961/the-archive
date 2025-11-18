import socket

def invert_vowel_words(message):
    vowels = 'aeiouAEIOU'
    words = message.split()
    inverted_message = []
    
    for word in words:
        if any(char in vowels for char in word):
            inverted_message.append(word[::-1])
        else:
            inverted_message.append(word)
    
    return ' '.join(inverted_message)

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
        
        # Invert words containing vowels and send back to the client
        response = invert_vowel_words(data)
        print(f"Server response: {response}")
        client_socket.send(response.encode('utf-8'))
        
        # Close the client socket
        client_socket.close()

if __name__ == "__main__":
    start_server()

