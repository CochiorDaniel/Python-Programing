import socket
import threading
import random

host = ''
port = 12346
barrier = threading.Barrier(2)
generated_number = None
lock = threading.Lock()
score = 0
maximum_score = 9999


def generate_random_number():
    global generated_number
    with lock:
        generated_number = random.randint(0, 50)


def handle_client1(client_socket, client_address):
    global generated_number
    try:
        while True:
            name = client_socket.recv(1024).decode("utf-8")
            print(f"Connection from {name} at {client_address}")

            greeting_message = f"Hello, {name}! Welcome to the server."
            client_socket.send(bytes(greeting_message, "utf-8"))
    except Exception as e:
        print(f"Error handling client {client_socket}: {e}")


def handle_client2(client_socket, client_address):
    global generated_number, score, maximum_score
    if generated_number is None:
        generate_random_number()
    print(f"Generated number: {generated_number}")
    try:
        while True:
            guess = client_socket.recv(1024).decode("utf-8")
            print(f"Received guess: {guess}")

            if int(guess) == generated_number:
                message = "Congratulations! You guessed the number!"
                client_socket.send(bytes(message, "utf-8"))
                break
            elif int(guess) < generated_number:
                message = "The number is greater than your guess!"
            else:
                message = "The number is smaller than your guess!"
            client_socket.send(bytes(message, "utf-8"))
            score += 1
        maximum_score = min(maximum_score, score)
        client_socket.send(bytes(f"Your score is {score}.", "utf-8"))
        client_socket.send(bytes(f"The maximum score is {maximum_score}.", "utf-8"))
        mesg = client_socket.recv(1024).decode("utf-8")
        mesg = client_socket.recv(1024).decode("utf-8")
        print(f"Received message: {mesg}")
        if mesg == "y":
            print("New game started!")
            score = 0
            generate_random_number()
            print(f"Generated number: {generated_number}")
            handle_client2(client_socket, client_address)
        else:
            print("Game ended!")
            client_socket.send(bytes(f"The maximum score is {maximum_score}.", "utf-8"))
            client_socket.close()
    except Exception as e:
        print(f"Error handling client {client_socket}: {e}")


def handle_client(client_socket, client_address, client_type):
    global generated_number
    try:
        if client_type == "generate_number":
            print("S-a conectat client de tip generate_number")
            handle_client1(client_socket, client_address)
        elif client_type == "guess_number":
            print("S-a conectat client de tip guess_number")
            handle_client2(client_socket, client_address)
    except Exception as e:
        print(f"Error handling client {client_socket}: {e}")


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print("Server listening for connections...")

    while True:
        client_socket, client_address = server_socket.accept()
        client_type = client_socket.recv(1024).decode("utf-8")
        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address, client_type))
        client_handler.start()


if __name__ == "__main__":
    main()
