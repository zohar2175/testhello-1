import socket

def start_client(server_ip):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, 12345))

    while True:
        message = input("Enter message to send (type 'quit' to exit): ")
        if message.lower() == 'quit':
            break

        client_socket.sendall(message.encode())
        data = client_socket.recv(1024)
        print(f"Echo from server: {data.decode()}")

    client_socket.close()

if __name__ == "__main__":
    server_ip = input("Enter server IP address: ")
    start_client(server_ip)