#ifndef BATTLESHIP_H_
#define BATTLESHIP_H_


#include <string>
#include <unordered_map>
#include <utility>  // for std::pair
#include "board.h"
#include "../socketserver.h"

using namespace std;
using namespace Sync;


class battleship {
	public:
		// game variables
		static const unordered_map<char, string> symbolToShip;
		bool isGameOver;
		bool isP1Turn;

		// player 1 variables
		string p1;
		board p1Ships;
		board p1Guesses;
		unordered_map<string, int> p1ShipStatus;

		// player 2 variables
		string p2;
		board p2Ships;
		board p2Guesses;
		unordered_map<string, int> p2ShipStatus;

		battleship();
		static void flushCout(int numLines = 50);
		static pair<int, int> parseCoordinatesInput(string input);
		static pair<int, int> getCoordinates(Socket& player);
		// static tuple<pair <int, int>, pair <int, int>> getCoordinates(int size);
		// static string getRandomCoordinates();
		// static string getRandomCoordinates(pair<int, int> coord, int size);
		// void getPlayerNames();
		void placeShips();
		void gameStep(
				Socket& p1Socket,
    			Socket& p2Socket
		);
		string gameStateToJSONString(int player);
		string fireAtCoordinates(int y, int x, int player);
};


#endif
