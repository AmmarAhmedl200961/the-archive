import socket
import threading

def handle_client(client_socket):
    with open('Voters_List.txt', 'r') as file:
        registered_voters = file.read().splitlines()

    voter_info = client_socket.recv(1024).decode('utf-8').strip()
    name, cnic = voter_info.split('/')
    voter_id = f"{name}/{cnic}"

    if voter_id in registered_voters:
        client_socket.send("Welcome, authenticated voter!\n".encode('utf-8'))

        with open('Candidates_List.txt', 'r') as file:
            candidates = file.read()

        client_socket.send(candidates.encode('utf-8'))

        poll_symbol = client_socket.recv(1024).decode('utf-8').strip()
        with open('Voting_Record.txt', 'a') as file:
            file.write(f"{voter_id} voted for {poll_symbol}\n")

        client_socket.send("Thank you for casting your vote!".encode('utf-8'))
    else:
        client_socket.send("Authentication failed. You are not registered.".encode('utf-8'))

    client_socket.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 9999))
server.listen(5)

print("Server started and waiting for connections...")
while True:
    client_socket, addr = server.accept()
    print(f"Connected to {addr}")
    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()

