import tkinter as tk
import tkinter.messagebox as mb

# Placeholder for the oxo_logic module if it's missing
class oxo_logic:
    @staticmethod
    def userMove(game, index):
        if game[index] == " ":
            game[index] = "X"
            return None
        return "Invalid"

    @staticmethod
    def computerMove(game):
        for i in range(len(game)):
            if game[i] == " ":
                game[i] = "O"
                return None
        return "D"  # Assume draw if no moves are left


top = tk.Tk()
top.title("Tic Tac Toe")

# Define menu functions
def evNew():
    global gameover
    gameover = False
    for row in range(3):
        for col in range(3):
            board.grid_slaves(row=row, column=col)[0]["text"] = " "
    status.config(text="Game Reset!")

def evResume():
    mb.showinfo("Resume", "Resume functionality not implemented.")

def evSave():
    mb.showinfo("Save", "Save functionality not implemented.")

def evExit():
    top.quit()

def evHelp():
    mb.showinfo("Help", "This is a simple Tic Tac Toe game. Try to win!")

def evAbout():
    mb.showinfo("About", "Tic Tac Toe Game\nVersion 1.0\nBy Your Name")

# Game logic
gameover = False

def evClick(row, col):
    global gameover
    if gameover:
        mb.showerror("Game Over", "The game is over! Start a new game.")
        return

    game = cells2game()
    index = (3 * row) + col
    result = oxo_logic.userMove(game, index)

    if result == "Invalid":
        mb.showerror("Invalid Move", "This cell is already occupied!")
        return

    game2cells(game)

    # Check for computer's move or game result
    result = oxo_logic.computerMove(game)
    game2cells(game)

    if result == "D":
        mb.showinfo("Result", "It's a Draw!")
        gameover = True
    elif result in ["X", "O"]:
        mb.showinfo("Result", f"The winner is: {result}")
        gameover = True

def game2cells(game):
    for row in range(3):
        for col in range(3):
            board.grid_slaves(row=row, column=col)[0]["text"] = game[3 * row + col]

def cells2game():
    values = []
    for row in range(3):
        for col in range(3):
            values.append(board.grid_slaves(row=row, column=col)[0]["text"])
    return values

# Build menu
def buildMenu(parent):
    menus = [
        ("File", [("New", evNew), ("Resume", evResume), ("Save", evSave), ("Exit", evExit)]),
        ("Help", [("Help", evHelp), ("About", evAbout)]),
    ]

    menubar = tk.Menu(parent)
    for menu in menus:
        m = tk.Menu(menubar, tearoff=0)
        for item in menu[1]:
            m.add_command(label=item[0], command=item[1])
        menubar.add_cascade(label=menu[0], menu=m)

    return menubar

# Build board
def buildBoard(parent):
    outer = tk.Frame(parent, border=2, relief="sunken")
    outer.pack()
    for row in range(3):
        for col in range(3):
            cell = tk.Button(
                outer,
                text=" ",
                width=5,
                height=2,
                command=lambda r=row, c=col: evClick(r, c),
            )
            cell.grid(row=row, column=col)
    return outer

# Main application setup
mbar = buildMenu(top)
top.config(menu=mbar)

board = buildBoard(top)

status = tk.Label(top, text="Welcome to Tic Tac Toe!", border=0, background="lightgrey", foreground="red")
status.pack(anchor="s", fill="x", expand=True)

top.mainloop()
