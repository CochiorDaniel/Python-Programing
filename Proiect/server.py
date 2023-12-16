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
sent_to = []
asteapta_numarul = threading.Event()


def generate_random_number():
    global generated_number
    with lock:
        generated_number = random.randint(0, 50)


def sent_to_all(message):
    global sent_to
    try:
        for client_socket in sent_to:
            client_socket.send(bytes(message, "utf-8"))
    except Exception as e:
        print(f"Error handling client {client_socket}: {e}")


def sent_to_client1(message):
    global sent_to
    try:
        sent_to[0].send(bytes(message, "utf-8"))
    except Exception as e:
        print(f"Error handling client {sent_to[0]}: {e}")


def sent_to_client2(message):
    global sent_to
    try:
        sent_to[1].send(bytes(message, "utf-8"))
    except Exception as e:
        print(f"Error handling client {sent_to[1]}: {e}")


def disconnect_all():
    global sent_to
    try:
        for client_socket in sent_to:
            client_socket.close()
    except Exception as e:
        print(f"Error handling client {client_socket}: {e}")


def handle_client1(client_socket):
    global generated_number
    print("Apelu e bun")
    try:
        # message = "Enter a number between 0 and 50: "
        # client_socket.send(bytes(message, "utf-8"))
        number = client_socket.recv(1024).decode("utf-8")
        print(f"Received message: {number}")
        with lock:
            generated_number = int(number)
        print(f"Generated number: {generated_number}")
        # asteapta_numarul.set()
    except Exception as e:
        print(f"Error handling client {client_socket}: {e}")


def handle_client2(client_socket, client_address):
    global generated_number, score, maximum_score, sent_to
    if generated_number is None:
        generate_random_number()
    print(f"Generated number: {generated_number}")
    try:
        while True:
            guess = client_socket.recv(1024).decode("utf-8")
            print(f"Received guess: {guess}")

            if int(guess) == generated_number:
                message = "Congratulations! You guessed the number!"
                score += 1
                # client_socket.send(bytes(message, "utf-8"))
                sent_to_client2(message)
                break
            elif int(guess) < generated_number:
                message = "The number is greater than your guess!"
            else:
                message = "The number is smaller than your guess!"
            # client_socket.send(bytes(message, "utf-8"))
            sent_to_all(message)
            score += 1
        maximum_score = min(maximum_score, score)
        # sent_to_all(message)
        m1 = f"Your score is {score}. The maximum score is {maximum_score}."
        # client_socket.send(bytes(f"Your score is {score}.", "utf-8"))
        # client_socket.send(bytes(f"The maximum score is {maximum_score}.", "utf-8"))
        sent_to_all(m1)
        mesg = client_socket.recv(1024).decode("utf-8")
        mesg = client_socket.recv(1024).decode("utf-8")
        print(f"Received message: {mesg}")
        if mesg == "y":
            print("New game started!")
            sent_to_client1(message)
            score = 0
            if len(sent_to) == 2:
                print("Apelez handle_client1")
                handle_client1(sent_to[0])
            else:
                generate_random_number()
            print(f"Generated number: {generated_number}")
            # asteapta_numarul.wait()
            # asteapta_numarul.clear()
            handle_client2(client_socket, client_address)
        else:
            print("Game ended!")
            m2 = f"Game ended! The maximum score is {maximum_score}."
            #client_socket.send(bytes(f"Game ended! The maximum score is {maximum_score}.", "utf-8"))
            sent_to_all(m2)
            disconnect_all()
            sent_to.clear()
    except Exception as e:
        print(f"Error handling client {client_socket}: {e}")


def handle_client(client_socket, client_address, client_type):
    global generated_number
    try:
        if client_type == "generate_number":
            print("S-a conectat client de tip generate_number")
            handle_client1(client_socket)
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
        sent_to.append(client_socket)
        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address, client_type))
        client_handler.start()


if __name__ == "__main__":
    main()
