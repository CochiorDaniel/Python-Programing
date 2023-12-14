import socket


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 12346))

    client_socket.send(b"guess_number")
    message = "lololo"
    while True:
        if message == "Congratulations! You guessed the number!":
            guess = "ceva"
            client_socket.send(bytes(guess, "utf-8"))
            guess = input("Do you want another game? y/n: ")
            client_socket.send(bytes(guess, "utf-8"))
            if guess == "n":
                message = client_socket.recv(1024).decode("utf-8")
                print(message)
                break
        else:
            guess = input("Enter your guess: ")
            client_socket.send(bytes(guess, "utf-8"))

        message = client_socket.recv(1024).decode("utf-8")
        print(f"Server: {message}")

    client_socket.close()


if __name__ == "__main__":
    main()

