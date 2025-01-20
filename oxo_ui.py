''' CLI User Interface for Tic-Tac-Toe game.
    Use as the main program, no reusable functions '''

# Placeholder for oxo_logic module if it's missing
class oxo_logic:
    @staticmethod
    def newGame():  
        return [" "] * 9

    @staticmethod
    def restoreGame():
        print("No saved game found. Starting a new game.")
        return oxo_logic.newGame()

    @staticmethod
    def saveGame(game):
        print("Game saved successfully!")

    @staticmethod
    def userMove(game, cell):
        if game[cell] == " ":
            game[cell] = "X"
            return None
        raise ValueError("Cell already occupied")

    @staticmethod
    def computerMove(game):
        for i in range(len(game)):
            if game[i] == " ":
                game[i] = "O"
                return None
        return "D"  # Return draw if no moves are left


# Menu options
menu = [
    "Start new game",
    "Resume saved game",
    "Display help",
    "Quit",
]

def getMenuChoice(aMenu):
    ''' getMenuChoice(aMenu) -> int

        Takes a list of strings as input,
        displays as a numbered menu and
        loops until the user selects a valid number '''
    
    if not aMenu:
        raise ValueError('No menu content')
    
    while True:
        print("\nMain Menu:")
        for index, item in enumerate(aMenu, start=1):
            print(f"{index}\t{item}")
        try:
            choice = int(input("\nChoose a menu option: "))
            if 1 <= choice <= len(aMenu):
                return choice
            else:
                print(f"Choose a number between 1 and {len(aMenu)}")
        except ValueError:
            print("Choose the number of a menu option")

def startGame():
    return oxo_logic.newGame()

def resumeGame():
    return oxo_logic.restoreGame()

def displayHelp():
    print('''
    Start new game:  Starts a new game of tic-tac-toe.
    Resume saved game: Restores the last saved game and commences play.
    Display help: Shows this page.
    Quit: Quits the application.
    ''')

def quitGame():
    print("Goodbye...")
    raise SystemExit

def executeChoice(choice):
    ''' executeChoice(int) -> None

        Execute whichever option the user selected.
        If the choice produces a valid game, then
        play the game until it completes. '''
    
    dispatch = [startGame, resumeGame, displayHelp, quitGame]
    game = dispatch[choice - 1]()
    if game:
        playGame(game)

def printGame(game):
    display = '''
      1 | 2 | 3      {} | {} | {}
     ----------     -----------
      4 | 5 | 6      {} | {} | {}
     ----------     -----------
      7 | 8 | 9      {} | {} | {}
    '''
    print(display.format(*game))

def playGame(game):
    result = ""
    while not result:
        printGame(game)
        choice = input("Choose a cell [1-9 or q to quit]: ")
        if choice.lower() == 'q':
            save = input("Save game before quitting? [y/n]: ")
            if save.lower() == 'y':
                oxo_logic.saveGame(game)
            quitGame()
        else:
            try:
                cell = int(choice) - 1
                if not (0 <= cell <= 8):  # Check range
                    raise ValueError
            except ValueError:
                print("Choose a number between 1 and 9 or 'q' to quit.")
                continue

            try:
                result = oxo_logic.userMove(game, cell)
            except ValueError:
                print("Cell already occupied. Choose an empty cell.")
                continue

            # Computer's move
            if not result:
                result = oxo_logic.computerMove(game)

            # Check result
            if result == "D":
                printGame(game)
                print("It's a draw!")
            elif result in ["X", "O"]:
                printGame(game)
                print(f"Winner is {result}!\n")

def main():
    while True:
        choice = getMenuChoice(menu)
        executeChoice(choice)

if __name__ == "__main__":
    main()
