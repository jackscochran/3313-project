############# BASE Info################
import os
boardX = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5,
          "F": 6, "G": 7, "H": 8, "I": 9, "J": 10}
boardY = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
board = ["A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1", "I1", "J1", "A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2", "I2", "J2", "A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3", "I3", "J3", "A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4", "I4", "J4", "A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5", "I5", "J5",
         "A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6", "I6", "J6", "A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7", "I7", "J7", "A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8", "I8", "J8", "A9", "B9", "C9", "D9", "E9", "F9", "G9", "H9", "I9", "J9", "A10", "B10", "C10", "D10", "E10", "F10", "G10", "H10", "I10", "J10"]
error_message = "Entry is not valid, try again"
rules = """\
Prepare for Battle:
Secretly place your fleet of 5 ships on your grid. To place each ship choose grid location start and end grid location.  Locations must be adjacent to each other.

How to Play:
You and your opponent will alternate turns, typing out one shot per turn to try and hit each other's ships.

Winning The Game:
If you're the first player to sink your opponent's entire fleet of 5 ship, you win the game!

"""
initialboard = """\
{A1}	{B1}	{C1}	{D1}	{E1}	{F1}	{G1}	{H1}	{I1}	{J1}
{A2}	{B2}	{C2}	{D2}	{E2}	{F2}	{G2}	{H2}	{I2}	{J2}
{A3}	{B3}	{C3}	{D3}	{E3}	{F3}	{G3}	{H3}	{I3}	{J3}
{A4}	{B4}	{C4}	{D4}	{E4}	{F4}	{G4}	{H4}	{I4}	{J4}
{A5}	{B5}	{C5}	{D5}	{E5}	{F5}	{G5}	{H5}	{I5}	{J5}
{A6}	{B6}	{C6}	{D6}	{E6}	{F6}	{G6}	{H6}	{I6}	{J6}
{A7}	{B7}	{C7}	{D7}	{E7}	{F7}	{G7}	{H7}	{I7}	{J7}
{A8}	{B8}	{C8}	{D8}	{E8}	{F8}	{G8}	{H8}	{I8}	{J8}
{A9}	{B9}	{C9}	{D9}	{E9}	{F9}	{G9}	{H9}	{I9}	{J9}
{A10}	{B10}	{C10}	{D10}	{E10}	{F10}	{G10}	{H10}	{I10}	{J10}
"""

board1 = """\
{}	{}	{}	{}	{}	{}	{}	{}	{}	{}
{}	{}	{}	{}	{}	{}	{}	{}	{}	{}
{}	{}	{}	{}	{}	{}	{}	{}	{}	{}
{}	{}	{}	{}	{}	{}	{}	{}	{}	{}
{}	{}	{}	{}	{}	{}	{}	{}	{}	{}
{}	{}	{}	{}	{}	{}	{}	{}	{}	{}
{}	{}	{}	{}	{}	{}	{}	{}	{}	{}
{}	{}	{}	{}	{}	{}	{}	{}	{}	{}
{}	{}	{}	{}	{}	{}	{}	{}	{}	{}
{}	{}	{}	{}	{}	{}	{}	{}	{}	{}
"""
board2 = """\
{}	{}	{}	{}	{}	{}	{}	{}	{}	{}
{}	{}	{}	{}	{}	{}	{}	{}	{}	{}
{}	{}	{}	{}	{}	{}	{}	{}	{}	{}
{}	{}	{}	{}	{}	{}	{}	{}	{}	{}
{}	{}	{}	{}	{}	{}	{}	{}	{}	{}
{}	{}	{}	{}	{}	{}	{}	{}	{}	{}
{}	{}	{}	{}	{}	{}	{}	{}	{}	{}
{}	{}	{}	{}	{}	{}	{}	{}	{}	{}
{}	{}	{}	{}	{}	{}	{}	{}	{}	{}
{}	{}	{}	{}	{}	{}	{}	{}	{}	{}
"""

word_hit = """\
██   ██ ██ ████████ ██ 
██   ██ ██    ██    ██ 
███████ ██    ██    ██ 
██   ██ ██    ██       
██   ██ ██    ██    ██ 
"""

word_miss = """\
███    ███ ██ ███████ ███████ ██ 
████  ████ ██ ██      ██      ██ 
██ ████ ██ ██ ███████ ███████ ██ 
██  ██  ██ ██      ██      ██    
██      ██ ██ ███████ ███████ ██
"""

word_battleship = """\
██████   █████  ████████ ████████ ██      ███████ ███████ ██   ██ ██ ██████  
██   ██ ██   ██    ██       ██    ██      ██      ██      ██   ██ ██ ██   ██ 
██████  ███████    ██       ██    ██      █████   ███████ ███████ ██ ██████  
██   ██ ██   ██    ██       ██    ██      ██           ██ ██   ██ ██ ██      
██████  ██   ██    ██       ██    ███████ ███████ ███████ ██   ██ ██ ██      
                                                                            
"""


##########END OF BASE##########


# CLASS
class Players:
    def __init__(self, name):
        boardavailable = ["A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1", "I1", "J1", "A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2", "I2", "J2", "A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3", "I3", "J3", "A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4", "I4", "J4", "A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5", "I5",
                          "J5", "A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6", "I6", "J6", "A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7", "I7", "J7", "A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8", "I8", "J8", "A9", "B9", "C9", "D9", "E9", "F9", "G9", "H9", "I9", "J9", "A10", "B10", "C10", "D10", "E10", "F10", "G10", "H10", "I10", "J10"]
        board_confirmed = True
        destoryer_location = []
        submarine_location = []
        cruiser_location = []
        battleship_location = []
        carrier_location = []
        destroyer_complete = False
        submarine_complete = False
        cruiser_complete = False
        battleship_complete = False
        carrier_complete = False
        board_playing_game = ["A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1", "I1", "J1", "A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2", "I2", "J2", "A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3", "I3", "J3", "A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4", "I4", "J4", "A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5", "I5",
                              "J5", "A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6", "I6", "J6", "A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7", "I7", "J7", "A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8", "I8", "J8", "A9", "B9", "C9", "D9", "E9", "F9", "G9", "H9", "I9", "J9", "A10", "B10", "C10", "D10", "E10", "F10", "G10", "H10", "I10", "J10"]
        destroyer_sunk = False
        submarine_sunk = False
        cruiser_sunk = False
        battleship_sunk = False
        carrier_sunk = False
        self.name = name
        self.boardavailable = boardavailable
        self.board_confirmed = board_confirmed
        self.destoryer_location = destoryer_location
        self.submarine_location = submarine_location
        self.cruiser_location = cruiser_location
        self.battleship_location = battleship_location
        self.carrier_location = carrier_location
        self.destroyer_complete = destroyer_complete
        self.submarine_complete = submarine_complete
        self.cruiser_complete = cruiser_complete
        self.battleship_complete = battleship_complete
        self.carrier_complete = carrier_complete
        self.board_playing_game = board_playing_game
        self.destroyer_sunk = destroyer_sunk
        self.submarine_sunk = submarine_sunk
        self.cruiser_sunk = cruiser_sunk
        self.battleship_sunk = battleship_sunk
        self.carrier_sunk = carrier_sunk

    def destoryer(self):
        complete = False
        self.complete = complete
        destoyer_temp_location = []
        print("Destroyer Size is 2")
        destroyer_start = input("START TILE: ").upper()
        destroyer_end = input("END TILE: ").upper()
        if destroyer_start in self.boardavailable:
            if destroyer_end in self.boardavailable:
                if destroyer_start[0].upper() == destroyer_end[0].upper():
                    if int(destroyer_end[1:]) > int(destroyer_start[1:]) and int(destroyer_end[1:]) == int(destroyer_start[1:]) + 1:
                        destoyer_temp_location.append(destroyer_start)
                        destoyer_temp_location.append(destroyer_end)
                        complete = True
                    elif int(destroyer_start[1:]) > int(destroyer_end[1:]) and int(destroyer_start[1:]) == int(destroyer_end[1:]) + 1:
                        destoyer_temp_location.append(destroyer_start)
                        destoyer_temp_location.append(destroyer_end)
                        complete = True
                    else:
                        print_error()

                elif destroyer_start[1:] == destroyer_end[1:]:
                    if boardX[destroyer_end[0].upper()] > boardX[destroyer_start[0].upper()] and boardX[destroyer_end[0].upper()] == boardX[destroyer_start[0].upper()] + 1:
                        destoyer_temp_location.append(destroyer_start)
                        destoyer_temp_location.append(destroyer_end)
                        complete = True
                    elif boardX.get(destroyer_start[0].upper()) > boardX.get(destroyer_end[0].upper()) and boardX.get(destroyer_start[0].upper()) == boardX.get(destroyer_end[0].upper()) + 1:
                        destoyer_temp_location.append(destroyer_start)
                        destoyer_temp_location.append(destroyer_end)
                        complete = True
                    else:
                        print_error()

                else:
                    print_error()

            else:
                print_error()

        else:
            print_error()

        for i in destoyer_temp_location:
            if i not in self.boardavailable:
                complete = False
                print_error()
                break

        if complete == True:
            print("Tiles Destroyer Tiles:", destoyer_temp_location)
            tcomplete = False
            while tcomplete == False:
                confirm = input("Would you like to continue, yes or no? ")
                if confirm == "yes":
                    for i in destoyer_temp_location:
                        self.destoryer_location.append(i)
                    for i in destoyer_temp_location:
                        tindex = self.boardavailable.index(i)
                        self.boardavailable[tindex] = "[De]"
                    tcomplete = True
                    self.destroyer_complete = True
                elif confirm == "no":
                    complete = False
                    break
                else:
                    print("not an option try again")

    def submarine(self):
        complete = False
        self.complete = complete
        submarine_temp_location = []
        print("Submarine Size is 3")
        submarine_start = input("START TILE: ").upper()
        submarine_end = input("END TILE: ").upper()

        if submarine_start in self.boardavailable:
            if submarine_end in self.boardavailable:
                if submarine_start[0].upper() == submarine_end[0].upper():
                    if int(submarine_end[1:]) > int(submarine_start[1:]) and int(submarine_end[1:]) == int(submarine_start[1:]) + 2:
                        tnum = int(submarine_end[1:]) - 1
                        secondtile = submarine_start[0] + str(tnum)
                        submarine_temp_location.append(submarine_start)
                        submarine_temp_location.append(secondtile)
                        submarine_temp_location.append(submarine_end)
                        complete = True
                    elif int(submarine_start[1:]) > int(submarine_end[1:]) and int(submarine_start[1:]) == int(submarine_end[1:]) + 2:
                        tnum = int(submarine_start[1:]) - 1
                        secondtile = submarine_start[0] + str(tnum)
                        submarine_temp_location.append(submarine_start)
                        submarine_temp_location.append(secondtile)
                        submarine_temp_location.append(submarine_end)
                        complete = True
                    else:
                        print_error()

                elif submarine_start[1:] == submarine_end[1:]:
                    if boardX[submarine_end[0].upper()] > boardX[submarine_start[0].upper()] and boardX[submarine_end[0].upper()] == boardX[submarine_start[0].upper()] + 2:
                        tnum = boardX[submarine_end[0]] - 1
                        secondtile = getletter(tnum) + str(submarine_start[1:])
                        submarine_temp_location.append(submarine_start)
                        submarine_temp_location.append(secondtile)
                        submarine_temp_location.append(submarine_end)
                        complete = True
                    elif boardX.get(submarine_start[0].upper()) > boardX.get(submarine_end[0].upper()) and boardX.get(submarine_start[0].upper()) == boardX.get(submarine_end[0].upper()) + 2:
                        tnum = boardX.get(submarine_start[0].upper()) - 1
                        secondtile = getletter(tnum) + str(submarine_start[1:])
                        submarine_temp_location.append(submarine_start)
                        submarine_temp_location.append(secondtile)
                        submarine_temp_location.append(submarine_end)
                        complete = True
                    else:
                        print_error()

                else:
                    print_error()

            else:
                print_error()

        else:
            print_error()

        for i in submarine_temp_location:
            if i not in self.boardavailable:
                complete = False
                print_error()
                break

        if complete == True:
            print("Tiles Submarine Tiles:", submarine_temp_location)
            tcomplete = False
            while tcomplete == False:
                confirm = input("Would you like to continue, yes or no? ")
                if confirm == "yes":
                    for i in submarine_temp_location:
                        self.submarine_location.append(i)
                    for i in submarine_temp_location:
                        tindex = self.boardavailable.index(i)
                        self.boardavailable[tindex] = "[Su]"
                    tcomplete = True
                    self.submarine_complete = True
                elif confirm == "no":
                    complete = False
                    break
                else:
                    print("not an option try again")

    def cruiser(self):
        complete = False
        self.complete = complete
        cruiser_temp_location = []
        print("Cruiser Size is 3")
        cruiser_start = input("START TILE: ").upper()
        cruiser_end = input("END TILE: ").upper()

        if cruiser_start in self.boardavailable:
            if cruiser_end in self.boardavailable:
                if cruiser_start[0].upper() == cruiser_end[0].upper():
                    if int(cruiser_end[1:]) > int(cruiser_start[1:]) and int(cruiser_end[1:]) == int(cruiser_start[1:]) + 2:
                        tnum = int(cruiser_end[1:]) - 1
                        secondtile = cruiser_start[0] + str(tnum)
                        cruiser_temp_location.append(cruiser_start)
                        cruiser_temp_location.append(secondtile)
                        cruiser_temp_location.append(cruiser_end)
                        complete = True
                    elif int(cruiser_start[1:]) > int(cruiser_end[1:]) and int(cruiser_start[1:]) == int(cruiser_end[1:]) + 2:
                        tnum = int(cruiser_start[1:]) - 1
                        secondtile = cruiser_start[0] + str(tnum)
                        cruiser_temp_location.append(cruiser_start)
                        cruiser_temp_location.append(secondtile)
                        cruiser_temp_location.append(cruiser_end)
                        complete = True
                    else:
                        print_error()

                elif cruiser_start[1:] == cruiser_end[1:]:
                    if boardX[cruiser_end[0].upper()] > boardX[cruiser_start[0].upper()] and boardX[cruiser_end[0].upper()] == boardX[cruiser_start[0].upper()] + 2:
                        tnum = boardX[cruiser_end[0]] - 1
                        secondtile = getletter(tnum) + str(cruiser_start[1:])
                        cruiser_temp_location.append(cruiser_start)
                        cruiser_temp_location.append(secondtile)
                        cruiser_temp_location.append(cruiser_end)
                        complete = True
                    elif boardX.get(cruiser_start[0].upper()) > boardX.get(cruiser_end[0].upper()) and boardX.get(cruiser_start[0].upper()) == boardX.get(cruiser_end[0].upper()) + 2:
                        tnum = boardX.get(cruiser_start[0].upper()) - 1
                        secondtile = getletter(tnum) + str(cruiser_start[1:])
                        cruiser_temp_location.append(cruiser_start)
                        cruiser_temp_location.append(secondtile)
                        cruiser_temp_location.append(cruiser_end)
                        complete = True
                    else:
                        print_error()

                else:
                    print_error()

            else:
                print_error()

        else:
            print_error()

        for i in cruiser_temp_location:
            if i not in self.boardavailable:
                complete = False
                print_error()
                break

        if complete == True:
            print("Tiles Cruiser Tiles:", cruiser_temp_location)
            tcomplete = False
            while tcomplete == False:
                confirm = input("Would you like to continue, yes or no? ")
                if confirm == "yes":
                    for i in cruiser_temp_location:
                        self.cruiser_location.append(i)
                    for i in cruiser_temp_location:
                        tindex = self.boardavailable.index(i)
                        self.boardavailable[tindex] = "[Cr]"
                    tcomplete = True
                    self.cruiser_complete = True
                elif confirm == "no":
                    complete = False
                    break
                else:
                    print("not an option try again")

    def battleship(self):
        complete = False
        self.complete = complete
        battleship_temp_location = []
        print("Battleship Size is 4")
        battleship_start = input("START TILE: ").upper()
        battleship_end = input("END TILE: ").upper()

        if battleship_start in self.boardavailable:
            if battleship_end in self.boardavailable:
                if battleship_start[0].upper() == battleship_end[0].upper():
                    if int(battleship_end[1:]) > int(battleship_start[1:]) and int(battleship_end[1:]) == int(battleship_start[1:]) + 3:
                        tnum = int(battleship_end[1:]) - 2
                        secondtile = battleship_start[0] + str(tnum)
                        tnum2 = int(battleship_end[1:]) - 1
                        thirdtile = battleship_start[0] + str(tnum2)
                        battleship_temp_location.append(battleship_start)
                        battleship_temp_location.append(secondtile)
                        battleship_temp_location.append(thirdtile)
                        battleship_temp_location.append(battleship_end)
                        complete = True
                    elif int(battleship_start[1:]) > int(battleship_end[1:]) and int(battleship_start[1:]) == int(battleship_end[1:]) + 3:
                        tnum = int(battleship_start[1:]) - 2
                        secondtile = battleship_start[0] + str(tnum)
                        tnum2 = int(battleship_start[1:]) - 1
                        thirdtile = battleship_start[0] + str(tnum2)
                        battleship_temp_location.append(battleship_start)
                        battleship_temp_location.append(thirdtile)
                        battleship_temp_location.append(secondtile)
                        battleship_temp_location.append(battleship_end)
                        complete = True
                    else:
                        print_error()

                elif battleship_start[1:] == battleship_end[1:]:
                    if boardX[battleship_end[0].upper()] > boardX[battleship_start[0].upper()] and boardX[battleship_end[0].upper()] == boardX[battleship_start[0].upper()] + 3:
                        tnum = boardX[battleship_end[0]] - 2
                        secondtile = getletter(
                            tnum) + str(battleship_start[1:])
                        tnum2 = boardX[battleship_end[0]] - 1
                        thirdtile = getletter(
                            tnum2) + str(battleship_start[1:])
                        battleship_temp_location.append(battleship_start)
                        battleship_temp_location.append(secondtile)
                        battleship_temp_location.append(thirdtile)
                        battleship_temp_location.append(battleship_end)
                        complete = True
                    elif boardX.get(battleship_start[0].upper()) > boardX.get(battleship_end[0].upper()) and boardX.get(battleship_start[0].upper()) == boardX.get(battleship_end[0].upper()) + 3:
                        tnum = boardX.get(battleship_start[0].upper()) - 2
                        secondtile = getletter(
                            tnum) + str(battleship_start[1:])
                        tnum2 = boardX.get(battleship_start[0].upper()) - 1
                        thirdtile = getletter(
                            tnum2) + str(battleship_start[1:])
                        battleship_temp_location.append(battleship_start)
                        battleship_temp_location.append(thirdtile)
                        battleship_temp_location.append(secondtile)
                        battleship_temp_location.append(battleship_end)
                        complete = True
                    else:
                        print_error()

                else:
                    print_error()

            else:
                print_error()

        else:
            print_error()

        for i in battleship_temp_location:
            if i not in self.boardavailable:
                complete = False
                print_error()
                break

        if complete == True:
            print("Tiles Battleship Tiles:", battleship_temp_location)
            tcomplete = False
            while tcomplete == False:
                confirm = input("Would you like to continue, yes or no? ")
                if confirm == "yes":
                    for i in battleship_temp_location:
                        self.battleship_location.append(i)
                    for i in battleship_temp_location:
                        tindex = self.boardavailable.index(i)
                        self.boardavailable[tindex] = "[Ba]"
                    tcomplete = True
                    self.battleship_complete = True
                elif confirm == "no":
                    complete = False
                    break
                else:
                    print("not an option try again")

    def carrier(self):
        complete = False
        self.complete = complete
        carrier_temp_location = []
        print("Carrier Size is 5")
        carrier_start = input("START TILE: ").upper()
        carrier_end = input("END TILE: ").upper()

        if carrier_start in self.boardavailable:
            if carrier_end in self.boardavailable:
                if carrier_start[0].upper() == carrier_end[0].upper():
                    if int(carrier_end[1:]) > int(carrier_start[1:]) and int(carrier_end[1:]) == int(carrier_start[1:]) + 4:
                        tnum = int(carrier_end[1:]) - 3
                        secondtile = carrier_start[0] + str(tnum)
                        tnum2 = int(carrier_end[1:]) - 2
                        thirdtile = carrier_start[0] + str(tnum2)
                        tnum3 = int(carrier_end[1:]) - 1
                        fourthtile = carrier_start[0] + str(tnum3)
                        carrier_temp_location.append(carrier_start)
                        carrier_temp_location.append(secondtile)
                        carrier_temp_location.append(thirdtile)
                        carrier_temp_location.append(fourthtile)
                        carrier_temp_location.append(carrier_end)
                        complete = True
                    elif int(carrier_start[1:]) > int(carrier_end[1:]) and int(carrier_start[1:]) == int(carrier_end[1:]) + 4:
                        tnum = int(carrier_start[1:]) - 3
                        secondtile = carrier_start[0] + str(tnum)
                        tnum2 = int(carrier_start[1:]) - 2
                        thirdtile = carrier_start[0] + str(tnum2)
                        tnum3 = int(carrier_start[1:]) - 1
                        fourthtile = carrier_start[0] + str(tnum3)
                        carrier_temp_location.append(carrier_start)
                        carrier_temp_location.append(fourthtile)
                        carrier_temp_location.append(thirdtile)
                        carrier_temp_location.append(secondtile)
                        carrier_temp_location.append(carrier_end)
                        complete = True
                    else:
                        print_error()

                elif carrier_start[1:] == carrier_end[1:]:
                    if boardX[carrier_end[0].upper()] > boardX[carrier_start[0].upper()] and boardX[carrier_end[0].upper()] == boardX[carrier_start[0].upper()] + 4:
                        tnum = boardX[carrier_end[0]] - 3
                        secondtile = getletter(tnum) + str(carrier_start[1:])
                        tnum2 = boardX[carrier_end[0]] - 2
                        thirdtile = getletter(tnum2) + str(carrier_start[1:])
                        tnum3 = boardX[carrier_end[0]] - 1
                        fourthtile = getletter(tnum3) + str(carrier_start[1:])
                        carrier_temp_location.append(carrier_start)
                        carrier_temp_location.append(secondtile)
                        carrier_temp_location.append(thirdtile)
                        carrier_temp_location.append(fourthtile)
                        carrier_temp_location.append(carrier_end)
                        complete = True
                    elif boardX.get(carrier_start[0].upper()) > boardX.get(carrier_end[0].upper()) and boardX.get(carrier_start[0].upper()) == boardX.get(carrier_end[0].upper()) + 4:
                        tnum = boardX.get(carrier_start[0].upper()) - 3
                        secondtile = getletter(tnum) + str(carrier_start[1:])
                        tnum2 = boardX.get(carrier_start[0].upper()) - 2
                        thirdtile = getletter(tnum2) + str(carrier_start[1:])
                        tnum3 = boardX.get(carrier_start[0].upper()) - 1
                        fourthtile = getletter(tnum3) + str(carrier_start[1:])
                        carrier_temp_location.append(carrier_start)
                        carrier_temp_location.append(fourthtile)
                        carrier_temp_location.append(thirdtile)
                        carrier_temp_location.append(secondtile)
                        carrier_temp_location.append(carrier_end)
                        complete = True
                    else:
                        print_error()

                else:
                    print_error()

            else:
                print_error()

        else:
            print_error()

        for i in carrier_temp_location:
            if i not in self.boardavailable:
                complete = False
                print_error()
                break

        if complete == True:
            print("Tiles Carrier Tiles:", carrier_temp_location)
            tcomplete = False
            while tcomplete == False:
                confirm = input("Would you like to continue, yes or no? ")
                if confirm == "yes":
                    for i in carrier_temp_location:
                        self.carrier_location.append(i)
                    for i in carrier_temp_location:
                        tindex = self.boardavailable.index(i)
                        self.boardavailable[tindex] = "[Ca]"
                    tcomplete = True
                    self.carrier_complete = True
                elif confirm == "no":
                    complete = False
                    break
                else:
                    print("not an option try again")


# CLASS END


############ start functions ####
def getletter(number):
    for key, value in boardX.items():
        if value == number:
            return key


def print_updated_board(board, board2):
    print(board.format(*board2))


def print_error():
    print(error_message)


def combine_pieces(de, su, cr, ba, ca):
    combine_list = []
    for i in de, su, cr, ba, ca:
        for g in i:
            combine_list.append(g)
    return combine_list


def check_suken_ship(player, attack_choice):
    if player.destroyer_sunk == False:
        des_hit = 0
        for i in attack_choice:
            if i in player.destoryer_location:
                des_hit += 1
            if des_hit == 2:
                player.destroyer_sunk = True
                print("***You Sunk My Destroyer!***")
                break
    if player.submarine_sunk == False:
        sub_hit = 0
        for i in attack_choice:
            if i in player.submarine_location:
                sub_hit += 1
            if sub_hit == 3:
                player.submarine_sunk = True
                print("***You Sunk My Submarine!***")
                break
    if player.cruiser_sunk == False:
        cr_hit = 0
        for i in attack_choice:
            if i in player.cruiser_location:
                cr_hit += 1
            if cr_hit == 3:
                player.cruiser_sunk = True
                print("***You Sunk My Cruiser!***")
                break
    if player.battleship_sunk == False:
        ba_hit = 0
        for i in attack_choice:
            if i in player.battleship_location:
                ba_hit += 1
            if ba_hit == 4:
                player.battleship_sunk = True
                print("***You Sunk My Battleship!***")
                break
    if player.carrier_sunk == False:
        ca_hit = 0
        for i in attack_choice:
            if i in player.carrier_location:
                ca_hit += 1
            if ca_hit == 5:
                player.carrier_sunk = True
                print("***You Sunk My Carrier!***")
                break


def ship_statues(player):
    destroyer = ""
    submarine = ""
    cruiser = ""
    battleship = ""
    carrier = ""
    if player.destroyer_sunk == True:
        destroyer = "Sunk"
    elif player.destroyer_sunk == False:
        destroyer = "Alive"
    if player.submarine_sunk == True:
        submarine = "Sunk"
    elif player.submarine_sunk == False:
        submarine = "Alive"
    if player.cruiser_sunk == True:
        cruiser = "Sunk"
    elif player.cruiser_sunk == False:
        cruiser = "Alive"
    if player.battleship_sunk == True:
        battleship = "Sunk"
    elif player.battleship_sunk == False:
        battleship = "Alive"
    if player.carrier_sunk == True:
        carrier = "Sunk"
    elif player.carrier_sunk == False:
        carrier = "Alive"

    statements = """\
Enemy Ship Statues:
Destroyer: {des}
Submarine: {sub}
Cruiser: {cr}
Battleship: {ba}
Carrier: {ca}
        """.format(des=destroyer, sub=submarine, cr=cruiser, ba=battleship, ca=carrier)
    print(statements)


def check_winner(player):
    if player.destroyer_sunk == True and player.submarine_sunk == True and player.cruiser_sunk == True and player.battleship_sunk == True and player.carrier_sunk == True:
        return True
    else:
        return False


############ end of functions ############
#### GAME START####
print(word_battleship)
start_game = False
while start_game == False:
    start_input = input(
        "type s to start game or type i for Instructions: ").upper()
    if start_input == "I":
        print(rules)
    elif start_input == "S":
        start_game = True
os.system('cls')
player_1_name = input("Input Player 1 Name: ")
player_2_name = input("Input Player 2 Name: ")

player1 = Players(player_1_name)
player2 = Players(player_2_name)

print("Player 2 LOOK AWAY!")

ready = False
while ready == False:
    answer = input("Ready for Board Set-Up, yes or no ")
    if answer == "yes":
        ready = True


######### BOARD SETUP Player 1 ########
player1_board_list = player1.boardavailable
print(initialboard)

player1.destoryer()
while player1.destroyer_complete == False:
    player1.destoryer()
print(player1.destoryer_location)
print_updated_board(board1, player1_board_list)

player1.submarine()
while player1.submarine_complete == False:
    player1.submarine()
print(player1.submarine_location)
print_updated_board(board1, player1_board_list)

player1.cruiser()
while player1.cruiser_complete == False:
    player1.cruiser()
print(player1.cruiser_location)
print_updated_board(board1, player1_board_list)

player1.battleship()
while player1.battleship_complete == False:
    player1.battleship()
print(player1.battleship_location)
print_updated_board(board1, player1_board_list)

player1.carrier()
while player1.carrier_complete == False:
    player1.carrier()
print(player1.carrier_location)
print_updated_board(board1, player1_board_list)


ready = False
while ready == False:
    answer = input("Are you complete viewing your board? yes or no ")
    if answer == "yes":
        ready = True
        os.system('cls')


########### BOARD SETUP Player 2 ###########
print("Player 1 LOOK AWAY!")
ready = False
while ready == False:
    answer = input("Ready for Board Set-Up, yes or no ")
    if answer == "yes":
        ready = True


player2_board_list = player2.boardavailable
print(initialboard)

player2.destoryer()
while player2.destroyer_complete == False:
    player2.destoryer()
print(player2.destoryer_location)
print_updated_board(board2, player2_board_list)

player2.submarine()
while player2.submarine_complete == False:
    player2.submarine()
print(player2.submarine_location)
print_updated_board(board2, player2_board_list)

player2.cruiser()
while player2.cruiser_complete == False:
    player2.cruiser()
print(player2.cruiser_location)
print_updated_board(board2, player2_board_list)

player2.battleship()
while player2.battleship_complete == False:
    player2.battleship()
print(player2.battleship_location)
print_updated_board(board2, player2_board_list)

player2.carrier()
while player2.carrier_complete == False:
    player2.carrier()
print(player2.carrier_location)
print_updated_board(board2, player2_board_list)

ready = False
while ready == False:
    answer = input("Are you complete viewing your board? yes or no ")
    if answer == "yes":
        ready = True
        os.system('cls')

############### GAME START ###############
p1name = player1.name
p2name = player2.name
player1_game_board = player2.board_playing_game
player2_game_board = player1.board_playing_game
player1_attack_choice = []
player2_attack_choice = []
player1_piece_location = combine_pieces(player1.destoryer_location, player1.submarine_location,
                                        player1.cruiser_location, player1.battleship_location, player1.carrier_location)
player2_piece_location = combine_pieces(player2.destoryer_location, player2.submarine_location,
                                        player2.cruiser_location, player2.battleship_location, player2.carrier_location)
game_complete = False
player1_winner = False
player2_winner = False

while game_complete == False:
    player1_turn = True
    player2_turn = True
    while player1_turn == True:
        player2_turn = True
        print("-------------------------------------------------------------------------")
        print_updated_board(board2, player1_game_board)
        ship_statues(player2)
        print(p1name + "'s Turn")
        grid_choice1 = input("Pick Tile to Attack: ").upper()
        if grid_choice1 in board:
            if grid_choice1 not in player1_attack_choice:
                if grid_choice1 in player2_piece_location:
                    player1_attack_choice.append(grid_choice1)
                    player2_piece_location[player2_piece_location.index(
                        grid_choice1)] = "X"
                    player1_game_board[player1_game_board.index(
                        grid_choice1)] = "X"
                    print(word_hit)
                    player1_turn = False
                else:
                    player1_attack_choice.append(grid_choice1)
                    player1_game_board[player1_game_board.index(
                        grid_choice1)] = "O"
                    print(word_miss)
                    player1_turn = False
            else:
                print("Tile Already Attacked, Try Again")
        else:
            print("Invalid Entry, Try Again")

    check_suken_ship(player2, player1_attack_choice)
    player1_winner = check_winner(player2)
    if player1_winner == True:
        game_complete = True
        break

    while player2_turn == True:
        player1_turn = True
        print("-------------------------------------------------------------------------")
        print_updated_board(board1, player2_game_board)
        ship_statues(player1)
        print(p2name+"'s Turn")
        grid_choice2 = input("Pick Tile to Attack: ").upper()
        if grid_choice2 in board:
            if grid_choice2 not in player2_attack_choice:
                if grid_choice2 in player1_piece_location:
                    player2_attack_choice.append(grid_choice2)
                    player1_piece_location[player1_piece_location.index(
                        grid_choice2)] = "X"
                    player2_game_board[player2_game_board.index(
                        grid_choice2)] = "X"
                    print(word_hit)
                    player2_turn = False
                else:
                    player2_attack_choice.append(grid_choice2)
                    player2_game_board[player2_game_board.index(
                        grid_choice2)] = "O"
                    print(word_miss)
                    player2_turn = False
            else:
                print("Tile Already Attacked, Try Again")
        else:
            print("Invalid Entry, Try Again")

    check_suken_ship(player1, player2_attack_choice)
    player2_winner = check_winner(player1)
    if player2_winner == True:
        game_complete = True
        break


######## END GAME ########
if player1_winner == True:
    print(p1name + " Wins!")

else:
    print(p2name + " Wins!")

final_answer = input("View Boards? y or n: ").upper()
final_answer_done = False
while final_answer_done == False:
    if final_answer == "Y":
        print(p1name+"'s Board")
        print_updated_board(board1, player1_board_list)
        print(p2name+"'s Board")
        print_updated_board(board2, player2_board_list)
        final_quit = input("Press Enter to Quit")
        final_answer_done = True
    elif final_answer == "N":
        final_answer = True
        break
    else:
        print("Invalid Input Try Again")
