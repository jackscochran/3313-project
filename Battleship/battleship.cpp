#include <iostream>
#include <ctype.h>  //isdigit(), tolower()
#include <regex>
#include "battleship.h"
#include <fstream>
#include <string>
#include <vector>
#include <random>

using namespace std;


// CLASS THAT DEFINES THE OBJECT TO SEND TO CLIENT WHEN IT IS THEIR TURN.
class TurnInfo {
	public:
		string player;
		string enemy;
		board* ships;  
		board* guesses;
		unordered_map<string, int>* enemyShipStatus;

	TurnInfo(string p, string e, board* s, board* g, unordered_map<string, int>* ess) : player(p), enemy(e), ships(s), guesses(g), enemyShipStatus(ess)
	{}
};

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
	p1 = "Player One";
	p2 = "Player Two";

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
	if (input.size() != 2) {
		cout << "Enter valid coordinates such as A3: " << endl;
		return make_pair(-1, -1);
	}

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

	// not any of these formats 3a, 3A, a3, A3
	if (!hasDigit or col < 0 or col > 9) {
		cout << "Enter valid coordinates such as A3: " << endl;
		return make_pair(-1, -1);
	}

	// if here, valid input
	return make_pair(row, col);
}


// returns (row, col) coordinates upon successful input from user
pair <int, int> battleship::getCoordinates() {
	string response;
	cout << "Enter coordinates such as A3: " << endl;
	
	while (true) {
		//
		getline(cin, response);
		// CHANGE THIS TO A SOCKET WRITE AND READ
		//
		pair<int, int> coord = parseCoordinatesInput(response);
		if (coord.first == -1)
			continue;  // invalid input, repeat

		cout << "Confirm " << response << "? (y/n)" << endl;
		getline(cin, response);
		if (response != "y") {
			cout << "Enter coordinates such as A3: " << endl;
			continue;  // user wants to change choice, repeat
		}

		return coord;
	}
}


// CALLED OVER AND OVER AGAIN UNTIL GAME IS OVER
// execution of a player move (one iteration of game)
void battleship::gameStep() {
	string player;
	string enemy;
	board* guesses;
	board* ships;
	board* enemyShips;
	unordered_map<string, int>* enemyShipStatus;

	if (isP1Turn) {
		player = p1;
		enemy = p2;
		guesses = &p1Guesses;
		ships = &p1Ships;
		enemyShips = &p2Ships;
		enemyShipStatus = &p2ShipStatus;
	}
	else {
		player = p2;
		enemy = p1;
		guesses = &p2Guesses;
		ships = &p2Ships;
		enemyShips = &p1Ships;
		enemyShipStatus = &p1ShipStatus;
	}

	// socket.Write(turnInfo)
	printTurnInfo(player, enemy, ships, guesses, enemyShipStatus);
	cout << "\n\n(Choose coordinate to fire at) ";
	while (true) {
		// socket.Read()
		pair<int, int> coord = getCoordinates();
		if (fireAtCoordinates(coord.first, coord.second, player, enemy, guesses, enemyShips, enemyShipStatus))
			break;
	}


	if (isGameOver)
		return;

	
	// string response;
	// cout << "Press enter to hide your board before " << enemy << "'s turn" << endl;
	// getline(cin, response);
	// flushCout();
	isP1Turn = !isP1Turn;  // change state to P2(1)
}


// prints the relevant info to player at start of each turn
void battleship::printTurnInfo(string player, string enemy, board* ships,  board* guesses,
		unordered_map<string, int>* enemyShipStatus) {
	string response;
	// Create obj with the params
	TurnInfo currentTurn(player, enemy, ships, guesses, enemyShipStatus);

	// make all non-strings strings (2 boards, 1 hm)


	// socket.Write(currentTurn)
	// json j = {
	// 	{"player", player},
	// 	{"enemy", enemy}
	// };
	
	
	
	
	cout << player << "'s turn" << endl;
	cout << "Press enter to see your board and guesses (make sure " << enemy << " can't see now)" << endl;

	getline(cin, response);
	cout << "Here's the status of your ships so far" << endl;
	ships->printBoard();
	cout << "Here's your fires so far" << endl;
	guesses->printBoard();
	cout << enemy << " still has their: ";
	for (auto iter : *enemyShipStatus)
		cout << iter.first << "\t";
}


// returns true and updates boards on a valid fire, false if already fired there
bool battleship::fireAtCoordinates(int y, int x, string player, string enemy, board* guesses,
		board* enemyShips, unordered_map<string, int>* enemyShipStatus) {

	// case - already hit
	if (guesses->hardcodedGrid[y][x] == 'x') {
		cout << "Already hit there! Choose again" << endl;
		return false;
	}
	// case - already miss
	else if (guesses->hardcodedGrid[y][x] == 'o') {
		cout << "Already missed there! Choose again" << endl;
		return false;
	}
	// case - new miss
	else if (enemyShips->hardcodedGrid[y][x] == '-') {
		guesses->hardcodedGrid[y][x] = 'o';
		enemyShips->hardcodedGrid[y][x] = 'o';
		cout << "Miss!" << endl;
		return true;
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
			cout << "Congrats, you sunk " << enemy << "'s " << shipHit << endl;
			// game over if that was last ship
			if (enemyShipStatus->empty()) {
				cout << "Congrats, you sunk all " << enemy << "'s ships" << endl;
				cout << player << " wins!" << endl;
				isGameOver = true;
			}
		}
		return true;
	}
}