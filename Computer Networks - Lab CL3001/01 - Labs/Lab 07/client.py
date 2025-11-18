import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 9999))

name = input("Enter your name: ")
cnic = input("Enter your CNIC: ")

client.send(f"{name}/{cnic}".encode('utf-8'))
response = client.recv(1024).decode('utf-8')
print(response)

if "Welcome" in response:
    candidates = client.recv(1024).decode('utf-8')
    print("Candidates:")
    print(candidates)

    poll_symbol = input("Enter the poll symbol of your chosen candidate: ")
    client.send(poll_symbol.encode('utf-8'))

    confirmation = client.recv(1024).decode('utf-8')
    print(confirmation)

client.close()

