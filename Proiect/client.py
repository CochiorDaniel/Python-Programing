import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 12345))

    while True:
        name = input("Enter your name: ")
        client_socket.send(bytes(name, "utf-8"))

        greeting_message = client_socket.recv(1024).decode("utf-8")
        print(greeting_message)

        if name.lower() == 'exit':
            break

    client_socket.close()


if __name__ == "__main__":
    main()
