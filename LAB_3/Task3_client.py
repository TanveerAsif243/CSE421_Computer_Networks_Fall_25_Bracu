import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    message = input("Enter a message: ")
    client_socket.send(message.encode())
    # client_socket.send(response.encode())
    # client_socket.send(str(vowel_count).encode())

    response = client_socket.recv(1024).decode()
    vowel_count = client_socket.recv(1024).decode()
    print(f"Server response: {response}")
    print(f"Vowel Count: {vowel_count}")
# hii
    client_socket.close()

if __name__ == "__main__":
    start_client()
