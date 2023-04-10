#include <iostream>
#include "board.h"
#include "./nlohmann/json.hpp"

using json = nlohmann::json;
using namespace std;


// board constructor
board::board() {
	for (int i = 0; i < BOARDSIZE; i++) {
		for (int j = 0; j < BOARDSIZE; j++) {
			hardcodedGrid[i][j] = '-';
		}
	}
}


// prints the contents of the board
void board::printBoard() {
	cout << "\n  A B C D E F G H I J" << endl;  // column names
	for (int i = 0; i < BOARDSIZE; i++) {
		cout << i << " ";  // row name
		for (int j = 0; j < BOARDSIZE; j++) {
			cout << hardcodedGrid[i][j] << " ";
		}
		cout << endl;
	}
	cout << endl;
}

void board::autoPlaceShips() {
	hardcodedGrid[0][0] = 'p';
    hardcodedGrid[0][1] = 'p';
    hardcodedGrid[2][2] = 's';
    hardcodedGrid[2][3] = 's';
    hardcodedGrid[2][4] = 's';
    hardcodedGrid[4][1] = 'd';
    hardcodedGrid[5][1] = 'd';
    hardcodedGrid[6][1] = 'd';
    hardcodedGrid[5][4] = 'b';
    hardcodedGrid[5][5] = 'b';
    hardcodedGrid[5][6] = 'b';
    hardcodedGrid[5][7] = 'b';
    hardcodedGrid[8][3] = 'c';
    hardcodedGrid[8][4] = 'c';
    hardcodedGrid[8][5] = 'c';
    hardcodedGrid[8][6] = 'c';
    hardcodedGrid[8][7] = 'c';
}

json board::boardToJSON() {
    json grid = json::array();
    for (int i = 0; i < BOARDSIZE; i++) {
        grid.push_back(json::array());
        for(int j = 0; j < BOARDSIZE; j++) {
            grid[i].push_back(hardcodedGrid[i][j]);
        }
    }
    return grid;
}

// // returns true if ship was successfully placed at given coordinates, false otherwise
// bool board::placeShip(int y1, int x1, int y2, int x2, int shipSize, char shipSymbol) {
// 	int start;
// 	int end;
// 	bool isHorizontal = true;
// 	// placing ship horizontally
// 	if (y1 == y2) {
// 		// entered coordinate on right first
// 		if (x1 > x2) {
// 			start = x2;
// 			end = x1;
// 		}
// 		// entered coordinate on left first
// 		else {
// 			start = x1;
// 			end = x2;
// 		}
// 	}
// 	// placing ship vertically
// 	else if (x1 == x2) {
// 		isHorizontal = false;
// 		// entered coordinated on bottom first
// 		if (y1 > y2) {
// 			start = y2;
// 			end = y1;
// 		}
// 		// entered coordinate on top first
// 		else {
// 			start = y1;
// 			end = y2;
// 		}
// 	}
// 	// can't place ship diagonally
// 	else {
// 		cout << "Invalid placement. Try again" << endl;
// 		return false;
// 	}

// 	// coordinates don't reflect size of ship
// 	if (end - start + 1 != shipSize) {
// 		cout << "Coordinates don't match the ship size of " << shipSize << endl;
// 		return false;
// 	}

// 	// check none of coordinates are occupied by another ship
// 	for (int i = start; i <= end; i++) {
// 		if (isHorizontal) {
// 			if (grid[y1][i] != '-') {
// 				char col = 65 + i;  // 65 is ascii of uppercase A
// 				cout << "Can't place ship here. " << col << y1 << " is already occupied" << endl;
// 				return false;
// 			}
// 		}
// 		else {
// 			if (grid[i][x1] != '-') {
// 				char col = 65 + x1;
// 				cout << "Can't place ship here. " << col << i << " is already occupied" << endl;
// 				return false;
// 			}
// 		}
// 	}

// 	// update board with ship placement
// 	for (int i = start; i <= end; i++) {
// 		if (isHorizontal) {
// 			grid[y1][i] = shipSymbol;
// 		}
// 		else {
// 			grid[i][x1] = shipSymbol;
// 		}
// 	}

// 	// return successful placement
// 	return true;
// }
