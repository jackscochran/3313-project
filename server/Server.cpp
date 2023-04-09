#include "thread.h"
#include "socketserver.h"
#include "./Battleship/battleship.h"
#include <stdlib.h>
#include <time.h>
#include <list>
#include <vector>
#include <algorithm>

using namespace Sync;

class GameThread : public Thread {
    private:
    Socket& p1Socket;
    Socket& p2Socket;
    ByteArray data;

    public:
        GameThread(Socket& p1Socket, Socket& p2Socket) : p1Socket(p1Socket), p2Socket(p2Socket)
        {
            std::cout << "Game Thread Created" << std::endl;
            // game = new Game()
        } 

        long ThreadMain()
        {
            try
            {   
                battleship game;

                p1Socket.Write(ByteArray("player1")); // message is board and player status
                p2Socket.Write(ByteArray("player2"));           

                while(true)
                {
                    while (!game.isGameOver){
                        // game.gameStep(p1Socket, p2Socket);

                        if(game.isP1Turn)
                        {
                            cout << "Player 1's turn" << endl;
                            p1Socket.Read(data);
	                        p1Socket.Write(ByteArray(game.gameStateToJSONString(1)));
                            p1Socket.Read(data);

                            if(data.ToString() == "quit"){
                                cout << "Player 1 quit" << endl;
                                game.isGameOver = true;
                                break;
                            }

                            pair<int, int> coord = game.parseCoordinatesInput(data.ToString());
                            string result = game.fireAtCoordinates(coord.first, coord.second, 1);
                            while(result == "invalid"){
                                p1Socket.Write(ByteArray(result));

                                p1Socket.Read(data);
                                coord = game.parseCoordinatesInput(data.ToString());
                                game.fireAtCoordinates(coord.first, coord.second, 1);

                            }

                            if(result == "end"){
                                game.isGameOver = true;
                                p1Socket.Write(ByteArray("win"));
                                p2Socket.Write(ByteArray("lose"));
                                break;
                            }
                            p1Socket.Write(ByteArray(result));
                            game.isP1Turn = false;
                        }
                        else
                        {
                            cout << "Player 2's turn" << endl;
                            p2Socket.Read(data);
                            p2Socket.Write(ByteArray(game.gameStateToJSONString(2)));
                            p2Socket.Read(data);

                            if(data.ToString() == "quit"){
                                cout << "Player 2 quit" << endl;
                                game.isGameOver = true;
                                break;
                            }

                            pair<int, int> coord = game.parseCoordinatesInput(data.ToString());
                            string result = game.fireAtCoordinates(coord.first, coord.second, 2);
                            while(result == "invalid"){
                                p2Socket.Write(ByteArray(result));

                                p2Socket.Read(data);
                                coord = game.parseCoordinatesInput(data.ToString());
                                game.fireAtCoordinates(coord.first, coord.second, 2);

                            }

                            if(result == "end"){
                                game.isGameOver = true;
                                p2Socket.Write(ByteArray("win"));
                                p1Socket.Write(ByteArray("lose"));
                                break;
                            }
                            p2Socket.Write(ByteArray(result));
                            game.isP1Turn = true;
                        }
                    }
                    cout << "Game Over" << endl;
                    p1Socket.Write(ByteArray("closed"));
                    p2Socket.Write(ByteArray("closed"));
                    break;
                }

            }
            catch(TerminationException terminationException)
            {
                std::cout << "Termination exception from socket" << std::endl;
                return terminationException;
            }
            std::cout << "Socket Closed" << std::endl;
            return 0;
        }
};

class ServerThread : public Thread{
    private:
        SocketServer& server;
    public:
        ServerThread(SocketServer& server) : server(server)
        {
            std::cout << "I am a server." << std::endl;
            std::cout << "ENTER terminates server" << std::endl;
            std::cout.flush();
        }

        ~ServerThread()
        {   
            server.Shutdown();
        }

        virtual long ThreadMain()
        {
            try
            {
                while(1)
                {
                    // wait for p1 to connect

                    Socket* p1Connection = new Socket(server.Accept());
                    Socket& p1SocketRef = *p1Connection;
                    cout << "Player 1 connected" << endl;

                    // send message to p1 to wait for p2
                    p1SocketRef.Write(ByteArray("waiting"));

                    Socket* p2Connection = new Socket(server.Accept());
                    Socket& p2SocketRef = *p2Connection;
                    cout << "Player 2 connected" << endl;

                    new GameThread(p1SocketRef, p2SocketRef);
                }
            }
            catch(std::string err)
            {
                std::cout << "Closing Server" << std::endl;
            }
            return 0;
        }
};


int main(void)
{
    try
    {
    // Create Server
    SocketServer server(2000);
    
    // // Thread init
    ServerThread* serverThread = new ServerThread(server);

    // Using pre-made classes from lab resources
    FlexWait cinWaiter(1, stdin);
    cinWaiter.Wait();
    std::cin.get();

    // Shutdown and gracefully shutdown server

    delete serverThread;
    }
    catch(std::string err)
    {
        std::cout << "Please close previously connected clients" << std::endl;
    }

    return 0;
    
}
