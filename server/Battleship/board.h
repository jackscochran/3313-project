#ifndef BOARD_H_
#define BOARD_H_

#include "./nlohmann/json.hpp"
using json = nlohmann::json;

const int BOARDSIZE = 10;

class board {
	public:
		char hardcodedGrid[BOARDSIZE][BOARDSIZE];
		board();
		void printBoard();
		void autoPlaceShips();
		json boardToJSON();
		// bool placeShip(int y1, int x1, int y2, int x2, int shipSize, char shipSymbol);
};


#endif
