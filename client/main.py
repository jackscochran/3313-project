import socket
import json

def main():
    server_ip = '10.0.2.15'  # Replace with the server IP you want to connect to
    server_port = 2000  # Replace with the server port you want to connect to

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
            client_socket.send("ready".encode())
            gamestate = client_socket.recv(1024).decode()

            if(gamestate == "closed"):
                print("Game over, draw game")
                return

            if(gamestate == "lose"):
                print("You lost!")
                return

            gamestate = json.loads(gamestate)

            print("\n----------------------------------")
            print("Here's the status of your board so far:")
            displayBoard(gamestate["ships"])
            print("\nHere's your shots so far:")
            displayBoard(gamestate["guesses"])

            displayEnemyStatus(gamestate["enemyShipStatus"])

            print('\nEnter "QUIT" to exit the game.')

            move = getMove(gamestate["guesses"])
            print("You guessed: " + move)

            if(move == "QUIT"):
                client_socket.sendall("quit".encode())
                print("You quit the game")
                return

            client_socket.sendall(move.encode())
            result = client_socket.recv(1024).decode()
            while(result == "invalid"):
                print("Invalid move")
                move = getMove(gamestate["guesses"])
                client_socket.sendall(move.encode())
                result = client_socket.recv(1024).decode()

            if(result == "hit"):
                print("You hit a ship!")
            elif(result == "miss"):
                print("You missed!")
            elif(result == "sunk"):
                print("You sunk a ship!")
            elif(result == "win"):
                print("You won!")
                return
            elif(result == "lose"):
                print("You lost!")
                return

            print("Waiting for opponent to make a move...")


    except Exception as e:        
        print("Server closed")

    except KeyboardInterrupt:
        print("You quit the game")
        client_socket.send("quit".encode())
        
    finally:
        # Close the socket connection
        client_socket.close()
        print("Socket closed")

def getMove(guesses):
    # get input coordinates from user
    move = input("Enter your move (ex. B4): ").upper()

    # validate input
    columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    rows = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    if(move == "QUIT"):
        return move

    if(len(move) != 2):
        print("Invalid move")
        return getMove(guesses)
    
    if(move[0] not in columns):
        print("Invalid move, column must be between A and H")
        return getMove(guesses)
    
    if(move[1] not in rows):
        print("Invalid move, row must be between 0 and 9")
        return getMove(guesses)

    # check if move has already been made
    print(guesses[rows.index(move[1])][columns.index(move[0])])
    if(guesses[rows.index(move[1])][columns.index(move[0])] != 45):
        print("Invalid move, you have already guessed this location")
        return getMove(guesses)

    return move

def displayBoard(board):
    boardSize = 10

    print("\n  A B C D E F G H I J")  # column names
    for i in range(boardSize):
        print(i, end=" ")  # row name
        for j in range(boardSize):
            print(chr(board[i][j]), end=" ")
        print()
    print()


def displayEnemyStatus(status):
    print("Opponents current status:")
    for ship in status.keys():
        print(f"  {ship}: {status[ship]}")

if __name__ == "__main__":
    main()
