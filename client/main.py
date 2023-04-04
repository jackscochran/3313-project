import socket

def main():
    server_ip = '127.0.0.1'  # Replace with the server IP you want to connect to
    server_port = 8080  # Replace with the server port you want to connect to

    message = "Hello, Server!"

    # Create a socket object (IPv4, TCP)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        client_socket.connect((server_ip, server_port))
        print(f"Connected to server at {server_ip}:{server_port}")
        print(f"Joining waiting room...")

        response = client_socket.recv(1024).decode()
    
        if(response == "waiting"):
            print("Waiting for another player...")
            response = client_socket.recv(1024).decode()

        if(response =="closed"):
            print("Server closed")
            return

        print("Game has started!")

        if(response == "player1"):
            print("You are player 1")

        if(response == "player2"):
            print("You are player 2")
            print("Waiting for player 1 to make a move...")

        # start game loop
        while(True):
            gameState = client_socket.recv(1024).decode()

            if(gameState == "closed"):
                print("Server closed")
                return

            print("\n----------------------------------")
            print("Your board:")
            displayBoard(gameState["playerBoard"])

            print("\nOpponent's board:")
            displayBoard(gameState["opponentBoard"])

            move = getMove()

            if(move == "quit"):
                client_socket.sendall(move.encode())
                print("You quit the game")
                return

            client_socket.sendall(move.encode())


    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the socket connection
        client_socket.close()
        print("Socket closed")

def getMove():
    # get input coordinates from user
    move = input("Enter your move (ex. B4): ")

    # validate input
    if(move.length != 2):
        print("Invalid move")
        return getMove()
    
    if(move[0] < 'A' or move[0] > 'H'):
        print("Invalid move, column must be between A and H")
        return getMove()
    
    if(move[1] < '1' or move[1] > '10'):
        print("Invalid move, row must be between 1 and 10")
        return getMove()

    return move

def displayBoard(gameState):
    # display 2-d array on console with row and column labels

    # print column labels
    print("  A B C D E F G H")

    # print row labels and board
    for i in range(10):
        print(i+1, end=" ")
        for j in range(8):
            print(gameState[i][j], end=" ")
        print()

if __name__ == "__main__":
    main()
