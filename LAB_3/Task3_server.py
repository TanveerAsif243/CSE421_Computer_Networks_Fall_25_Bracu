import socket
import threading

def count_vowels(message):
    vowels = 'aeiouAEIOU'
    sum = 0
    for char in message :
        if char in vowels:
            sum+=1
    return sum

def handle_client(client_socket, client_address):
    print(f"Connection from {client_address}")

    message = client_socket.recv(1024).decode()
    vowel_count = count_vowels(message)

    if vowel_count == 0:
        response = " Not enough vowels"
    elif vowel_count <= 2:
        response = "Enough vowels I guess"
    else:
        response = "Too many vowels"

    client_socket.send(response.encode())
    # client_socket.send(response.encode())
    client_socket.send(str(vowel_count).encode())

    client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 12345))
    server_socket.listen(5)
    print("Server listening on port 12345")

    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == "__main__":
    start_server()
