#include <iostream>
#include <string>
#include "battleship.h"

using namespace std;

// THIS WILL BE SUBSTITUTED WITH A GAME THREAD
int main() {
	cout << "Play battleship? (y/n)" << endl;
	string response;
	getline(cin, response);
	if (response != "y") {
		cout << "Farewell!" << endl;
		return 0;
	}

	// CALLS THE CAME TO START
	battleship game;
	while (!game.isGameOver)
		game.gameStep();

	return 0;
}
