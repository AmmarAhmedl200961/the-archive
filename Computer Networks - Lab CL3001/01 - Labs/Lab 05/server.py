import socket

# Server details
SERVER_IP = "127.0.0.1"
SERVER_PORT = 5006

# Create UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((SERVER_IP, SERVER_PORT))

print("Server is listening...")

# Read attendance data from file
def load_attendance():
    try:
        with open("attendance.txt", "r") as f:
            data = f.read().split()
            return data if data else []
    except FileNotFoundError:
        return []

# Write attendance data to file
def save_attendance(attendance_list):
    with open("attendance.txt", "w") as f:
        f.write(" ".join(attendance_list))

attendance_list = load_attendance()

while True:
    # Receive message from client
    client_message, client_address = server_socket.recvfrom(2048)
    client_message = client_message.decode()
    
    print(f"Received message from {client_address}: {client_message}")

    roll_number = client_message[:7]
    action = client_message[8:]  # CI (Check In) or CO (Check Out)

    server_response = ""
    if action == "CI":
        if roll_number not in attendance_list:
            attendance_list.append(roll_number)
            server_response = f"Welcome Student {roll_number}!"
            save_attendance(attendance_list)
        else:
            server_response = "You are already here."
    
    elif action == "CO":
        if roll_number in attendance_list:
            attendance_list.remove(roll_number)
            server_response = f"Goodbye Student {roll_number}! Have a nice day!"
            save_attendance(attendance_list)
        else:
            server_response = "You didn't check in today. Contact System Administrator."
    
    else:
        server_response = "Invalid action."

    # Send response back to client
    server_socket.sendto(server_response.encode(), client_address)
