import socket

def main():
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_address = ('127.0.0.1', 2000)

    try:
        # Get input from the user
        client_name = input("Enter your name: ")
        client_phone = input("Enter your phone number: ")
        client_message = f"{client_name},{client_phone}"
        
        # transmit client information to the server
        sock.sendto(client_message.encode(), server_address)

        # get welcome message and grocery list from the server
        server_message, _ = sock.recvfrom(2000)
        print(server_message.decode())

        server_message, _ = sock.recvfrom(2000)
        print(server_message.decode())

        # take input of grocery items to purchase
        while True:
            order_items = input("Enter the names of the grocery items you wish to purchase (comma-separated): ")
            sock.sendto(order_items.encode(), server_address)

            # Receive the response from the server
            server_message, _ = sock.recvfrom(2000)
            print(server_message.decode())

            if "Thank you" in server_message.decode():
                break

    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Close the socket
        sock.close()

if __name__ == "__main__":
    main()
