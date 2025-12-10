
import platform
import socket

def get_device_name():
    return platform.node()

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    ip = socket.gethostbyname(socket.gethostname())
    device_name = get_device_name()

    message = f"Client IP: {ip}, Device Name: {device_name}"
    client_socket.send(message.encode())

    client_socket.close()

if __name__ == "__main__":
    start_client()
