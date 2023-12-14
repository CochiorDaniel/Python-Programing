import socket
import threading


def handle_client(client_socket, client_address):
    try:
        while True:
            name = client_socket.recv(1024).decode("utf-8")
            print(f"Connection from {name} at {client_address}")

            greeting_message = f"Hello, {name}! Welcome to the server."
            client_socket.send(bytes(greeting_message, "utf-8"))
    except Exception as e:
        print(f"Error handling client {name}: {e}")


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(5)
    print("Server listening for connections...")

    while True:
        client_socket, client_address = server_socket.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_handler.start()


if __name__ == "__main__":
    main()
