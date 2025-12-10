import socket

def calculate_salary(hours_worked):
    if hours_worked <= 40:
        return hours_worked * 200
    else:
        return 8000 + (hours_worked - 40) * 300

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 12345))
    server_socket.listen(5)
    print("Server listening on port 12345")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        hours_worked = float(client_socket.recv(1024).decode())
        salary = calculate_salary(hours_worked)

        client_socket.send(str(salary).encode())
        client_socket.close()

if __name__ == "__main__":
    start_server()
