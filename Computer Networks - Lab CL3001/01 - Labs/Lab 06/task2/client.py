import socket

def invert_non_vowel_words(message):
    vowels = 'aeiouAEIOU'
    words = message.split()
    inverted_message = []
    
    for word in words:
        if not any(char in vowels for char in word):
            inverted_message.append(word[::-1])
        else:
            inverted_message.append(word)
    
    return ' '.join(inverted_message)

def start_client():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Define the host and port of the server
    host = '127.0.0.1'  # Localhost
    port = 8000
    
    # Connect to the server
    client_socket.connect((host, port))
    
    # Send a message to the server
    message = input("Enter a message: ")
    client_socket.send(message.encode('utf-8'))
    
    # Receive the response from the server
    response = client_socket.recv(1024).decode('utf-8')
    print(f"Server response: {response}")
    
    # Invert words without vowels and display
    final_message = invert_non_vowel_words(response)
    print(f"Client final output: {final_message}")
    
    # Close the client socket
    client_socket.close()

if __name__ == "__main__":
    start_client()

