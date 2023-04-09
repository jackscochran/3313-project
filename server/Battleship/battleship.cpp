#include <iostream>
#include <ctype.h>  //isdigit(), tolower()
#include <regex>
#include "battleship.h"
#include <fstream>
#include <string>
#include <vector>
#include <random>
#include "./nlohmann/json.hpp"
#include "../socketserver.h"

using json = nlohmann::json;
using namespace std;
using namespace Sync;


// HASH MAP OF SHIPS AND THEIR DESIGNATIONS (ABBRV.)
const unordered_map<char, string> battleship::symbolToShip = {
	{'c', "carrier"},
	{'b', "battleship"},
	{'d', "destroyer"},
	{'s', "submarine"},
	{'p', "patrol boat"}
};


// CONSTRUCTOR OF BATTLESHIP GAME
battleship::battleship() {
	// getPlayerNames();
	isGameOver = false;
	isP1Turn = true;

	p1ShipStatus = {
		{"carrier", 5},
		{"battleship", 4},
		{"destroyer", 3},
		{"submarine", 3},
		{"patrol boat", 2}
	};

	p2ShipStatus = {
		{"carrier", 5},
		{"battleship", 4},
		{"destroyer", 3},
		{"submarine", 3},
		{"patrol boat", 2}
	};

	placeShips();  // placing p1 ships SHOULD BE hardcoded NOW
	placeShips();  // placing p2 ships SHOULD BE hardcoded NOW
}


// clears std::cout when switching turns to prevent seeing opponent's board
void battleship::flushCout(int numLines) {
	for (int i = 0; i < numLines; i++)
		cout << endl;
}

void battleship::placeShips() {
	board* ships;
	if (isP1Turn) {
		ships = &p1Ships;
	}
	else {
		ships = &p2Ships;
	}
	ships->autoPlaceShips();
	isP1Turn = !isP1Turn;
	// flushCout();
}

// returns (-1, -1) if invalid input else (row, col) of coordinate input
pair<int, int> battleship::parseCoordinatesInput(string input) {

	bool hasDigit = false;
	int row;
	int col;

	// row number came first
	if (isdigit(input[0])) {
		hasDigit = true;
		col = (int) tolower(input[1]) - 97;  // ascii of lowercase a is 97
		row = (int) input[0] - 48;  // ascii of 0 is 48

	}
	// row number came second
	else if (isdigit(input[1])) {
		hasDigit = true;
		col = (int) tolower(input[0]) - 97;
		row = (int) input[1] - 48;
	}

	// if here, valid input
	return make_pair(row, col);
}


// returns (row, col) coordinates upon successful input from user
pair <int, int> battleship::getCoordinates(Socket& player) {

	ByteArray data;
	
	player.Read(data);
	pair<int, int> coord = parseCoordinatesInput(data.ToString());
	return coord;
}


// prints the relevant info to player at start of each turn
string battleship::gameStateToJSONString(int player) {
	board* guesses;
	board* ships;
	board* enemyShips;
	unordered_map<string, int>* enemyShipStatus;

	if (player == 1){
		guesses = &p1Guesses;
		ships = &p1Ships;
		enemyShipStatus = &p2ShipStatus;
	} else{
		guesses = &p2Guesses;
		ships = &p2Ships;
		enemyShipStatus = &p1ShipStatus;
	}

	// string response;

	// JSONIFY
	json s;
	for(auto it = enemyShipStatus->begin(); it != enemyShipStatus->end(); ++it) {
		s[it->first] = it->second; 
	}
	
	json turnInfo = {
		{"ships", ships->boardToJSON()},
		{"guesses", guesses->boardToJSON()},
		{"enemyShipStatus", s}
	};
	
	return turnInfo.dump();

}


// returns true and updates boards on a valid fire, false if already fired there
string battleship::fireAtCoordinates(int y, int x, int player) {
	board* guesses;
	board* enemyShips;
	unordered_map<string, int>* enemyShipStatus;

	if (player == 1){
		guesses = &p1Guesses;
		enemyShips = &p1Ships;
		enemyShipStatus = &p2ShipStatus;
	} else{
		guesses = &p2Guesses;
		enemyShips = &p2Ships;
		enemyShipStatus = &p1ShipStatus;
	}

	// case - already hit
	if (guesses->hardcodedGrid[y][x] == 'x') {
		cout << "Already hit there! Choose again" << endl;
		return "invalid";
	}
	// case - already miss
	else if (guesses->hardcodedGrid[y][x] == 'o') {
		cout << "Already missed there! Choose again" << endl;
		return "invalid";
	}
	// case - new miss
	else if (enemyShips->hardcodedGrid[y][x] == '-') {
		guesses->hardcodedGrid[y][x] = 'o';
		enemyShips->hardcodedGrid[y][x] = 'o';
		cout << "Miss!" << endl;
		return "miss";
	}
	// case - new hit
	else {
		char shipSymbol = enemyShips->hardcodedGrid[y][x];
		string shipHit = symbolToShip.at(shipSymbol);
		guesses->hardcodedGrid[y][x] = 'x';
		enemyShips->hardcodedGrid[y][x] = 'x';
		cout << "Hit! " << shipHit << "!" << endl;
		enemyShipStatus->operator[](shipHit)--;

		// if hit sinks ship
		if (enemyShipStatus->operator[](shipHit) == 0) {
			enemyShipStatus->erase(shipHit);
			// game over if that was last ship
			if (enemyShipStatus->empty()) {
				isGameOver = true;
				return "end"; // game over
			}
			return "sunk"; // sunk ship
		}
		return "hit"; // new hit
	}
}