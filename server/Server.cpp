#include "thread.h"
#include "socketserver.h"
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
    Game game;

    public:
        GameThread(Socket& p1Socket, Socket& p2Socket) : p1Socket(p1Socket), p2Socket(p2Socket)
        {
            std::cout << "Game Thread Created" << std::endl;
            game = new Game()
        } 

        long ThreadMain()
        {
            try
            {

                game.Start() // start game
                p1Socket.Write(ByteArray(message)); // message is board and player status
                p2Socket.Write(ByteArray(message));

                while(!game.isGameOver)
                {

                    game.gameStep();
                    // p1Socket.Read(data);

                    // std::string res = data.ToString();

                    // if(res=="done")
                    // {
                    //     break;
                    // }

                    // socket.Write(ByteArray(res));

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
                    Socket* p1Connection = new Socket(server.Accept());
                    Socket& p1SocketRef = *connection;

                    // send message to p1 to wait for p2

                    Socket* p2Connection = new Socket(server.Accept());
                    Socket& p2SocketRef = *connection;

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
