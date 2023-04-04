import socket

def main():
    server_ip = '127.0.0.1'  # Replace with the server IP you want to bind to
    server_port = 8080  # Replace with the server port you want to bind to

    # Create a socket object (IPv4, TCP)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Bind the socket to the IP and port
        server_socket.bind((server_ip, server_port))
        print(f"Server bound to {server_ip}:{server_port}")

        # Listen for incoming connections (backlog of 1)
        server_socket.listen(1)
        print("Server listening for connections...")

        while True:
            # Accept an incoming connection
            client_socket, client_addr = server_socket.accept()
            print(f"Connection from {client_addr[0]}:{client_addr[1]}")

            # Receive the message from the client
            message = client_socket.recv(1024)
            print(f"Received message: {message.decode()}")

            # Send a response to the client (optional)
            response = "Message received!"
            client_socket.sendall(response.encode())
            print(f"Response sent: {response}")

            # Close the client socket
            client_socket.close()
            print(f"Connection with {client_addr[0]}:{client_addr[1]} closed")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the server socket
        server_socket.close()
        print("Server socket closed")

if __name__ == "__main__":
    main()
