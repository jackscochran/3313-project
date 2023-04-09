all: Server

Server: Server.o thread.o socket.o socketserver.o Blockable.o battleship.o board.o
	g++ -o Server Server.o thread.o socket.o socketserver.o Blockable.o battleship.o board.o -pthread -l rt

Blockable.o: Blockable.h Blockable.cpp
	g++ -c Blockable.cpp -std=c++11

Server.o: Server.cpp thread.h socketserver.h ./Battleship/battleship.h
	g++ -c Server.cpp -std=c++11

thread.o: thread.cpp thread.h
	g++ -c thread.cpp -std=c++11

socket.o: socket.cpp socket.h
	g++ -c socket.cpp -std=c++11

socketserver.o: socketserver.cpp socket.h socketserver.h
	g++ -c socketserver.cpp -std=c++11

battleship.o: ./Battleship/battleship.cpp ./Battleship/battleship.h ./Battleship/board.h
	g++ -c ./Battleship/battleship.cpp -std=c++11

board.o: ./Battleship/board.cpp ./Battleship/board.h
	g++ -c ./Battleship/board.cpp -std=c++11
