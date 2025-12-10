import socket


def get_hours_worked():
    hours = input("Enter the worked hours: ")

    while True:
        is_valid = True
        if hours.count('.') > 1:
            is_valid = False
        else:
            for char in hours:
                if char not in "0123456789.":
                    is_valid = False
                    break

        if is_valid and float(hours) >= 0:
            return float(hours)
        else:
            hours = input("Invalid input. Please enter a valid number of hours worked (positive number): ")

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('localhost', 12345)
    client_socket.connect(server_address)

    hours_worked = get_hours_worked()


    client_socket.send(str(hours_worked).encode())      # Send hours worked to the server


    salary = client_socket.recv(1024).decode()
    print(f"The calculated salary is: {salary}")

    client_socket.close()


if __name__ == "__main__":
    start_client()
