import socket

def load_groceries(filename):
    groceries = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                item, price = line.split(' - ')
                groceries[item] = price
    except FileNotFoundError:
        print(f"File {filename} not found.")
    return groceries

def main():
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the server address and port
    server_address = ('127.0.0.1', 2000)
    sock.bind(server_address)

    print("Socket created and bound")
    print("Listening for messages...\n")

    groceries = load_groceries('groceries.txt')

    while True:
        try:
            # get client's name and phone number
            client_message, client_address = sock.recvfrom(2000)
            client_info = client_message.decode().split(',')
            client_name, client_phone = client_info[0], client_info[1]

            # welcome message
            welcome_message = f"Welcome, {client_name}! Your phone number is {client_phone}."
            sock.sendto(welcome_message.encode(), client_address)

            # show list of available grocery items
            grocery_list_message = "\nAvailable Grocery Items:\n"
            for item, price in groceries.items():
                grocery_list_message += f"{item} - {price}\n"
            sock.sendto(grocery_list_message.encode(), client_address)

            # get and verify the client's order
            while True:
                order_message, _ = sock.recvfrom(2000)
                order_items = order_message.decode().split(',')
                valid_items = [item.strip() for item in order_items if item.strip() in groceries]

                if not valid_items:
                    error_message = "Sorry! None of the items are available. Please choose from the available list."
                    sock.sendto(error_message.encode(), client_address)
                elif len(valid_items) != len(order_items):
                    error_message = "Sorry! Some items are not available. Please choose from the available list."
                    sock.sendto(error_message.encode(), client_address)
                else:
                    confirmation_message = "Thank you for your order! Your groceries will be delivered within 24 hours. Happy shopping!"
                    sock.sendto(confirmation_message.encode(), client_address)
                    break

        except Exception as e:
            print(f"An error occurred: {e}")
            break

    # Closing the socket
    sock.close()

if __name__ == "__main__":
    main()
