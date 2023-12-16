import socket


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 12346))

    client_socket.send(b"generate_number")
    number = input("Enter a number between 0 and 50: ")
    client_socket.send(bytes(number, "utf-8"))
    message = "lololo"
    while True:
        if "Game ended" in message:
            break
        if "Congratulations! You guessed the number!" in message or "Invalid number!" in message:
            number = input("Enter a number between 0 and 50: ")
            client_socket.send(bytes(number, "utf-8"))

        message = client_socket.recv(1024).decode("utf-8")
        print(message)

    client_socket.close()


if __name__ == "__main__":
    main()
