from tkinter import *

# ===== Game Variables =====
play_board = [["#"]*3 for _ in range(3)]
buttons = [[None]*3 for _ in range(3)]

Player1 = ""
Player2 = ""
current_player = ""
player1_name = ""
player2_name = ""

# ===== Win Condition =====
def WinCondition():
    # Player1 win check
    if (play_board[0][0] == Player1 and play_board[0][1] == Player1 and play_board[0][2] == Player1) or \
       (play_board[1][0] == Player1 and play_board[1][1] == Player1 and play_board[1][2] == Player1) or \
       (play_board[2][0] == Player1 and play_board[2][1] == Player1 and play_board[2][2] == Player1) or \
       (play_board[0][0] == Player1 and play_board[1][0] == Player1 and play_board[2][0] == Player1) or \
       (play_board[0][1] == Player1 and play_board[1][1] == Player1 and play_board[2][1] == Player1) or \
       (play_board[0][2]== Player1 and play_board[1][2] == Player1 and play_board[2][2] == Player1) or \
       (play_board[0][0] == Player1 and play_board[1][1] == Player1 and play_board[2][2] == Player1) or \
       (play_board[0][2] == Player1 and play_board[1][1] == Player1 and play_board[2][0] == Player1):
        return 1
    # Player2 win check
    elif (play_board[0][0]==Player2 and play_board[0][1]==Player2 and play_board[0][2]==Player2) or \
         (play_board[1][0]==Player2 and play_board[1][1]==Player2 and play_board[1][2]==Player2) or \
         (play_board[2][0]==Player2 and play_board[2][1]==Player2 and play_board[2][2]==Player2) or \
         (play_board[0][0]==Player2 and play_board[1][0]==Player2 and play_board[2][0]==Player2) or \
         (play_board[0][1]==Player2 and play_board[1][1]==Player2 and play_board[2][1]==Player2) or \
         (play_board[0][2]==Player2 and play_board[1][2]==Player2 and play_board[2][2]==Player2) or \
         (play_board[0][0]==Player2 and play_board[1][1]==Player2 and play_board[2][2]==Player2) or \
         (play_board[0][2]==Player2 and play_board[1][1]==Player2 and play_board[2][0]==Player2):
        return -1

# ===== Draw Condition =====
def check_draw():
    for row in play_board:
        if "#" in row:
            return False
    return True

# ===== Disable Buttons =====
def disable_buttons():
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(state="disabled")

# ===== On Click Function =====
def on_click(x, y):
    global current_player
    if play_board[x][y] == "#":
        play_board[x][y] = current_player
        buttons[x][y].config(text=current_player)
        result = WinCondition()
        if result == 1:
            Label(root, text=f"{player1_name} wins!", font=("Arial", 16, "bold"), bg="lightblue").grid(row=7, column=0, columnspan=3, pady=10)
            disable_buttons()
            show_end_buttons()
        elif result == -1:
            Label(root, text=f"{player2_name} wins!", font=("Arial", 16, "bold"), bg="lightblue").grid(row=7, column=0, columnspan=3, pady=10)
            disable_buttons()
            show_end_buttons()
        elif check_draw():
            Label(root, text="It's a Draw!", font=("Arial", 16, "bold"), bg="lightblue").grid(row=7, column=0, columnspan=3, pady=10)
            disable_buttons()
            show_end_buttons()
        else:
            current_player = Player2 if current_player == Player1 else Player1

# ===== Create Board =====
def create_board():
    for x in range(3):
        for y in range(3):
            btn = Button(root, text="", fg="white", bg="orange",
                         height=3, width=7, font=("Arial", 28, "bold"),
                         command=lambda x=x, y=y: on_click(x, y))
            buttons[x][y] = btn
            btn.grid(column=y, row=x+3, padx=5, pady=5)

# ===== Show Player Info =====
def show_player_info():
    Label(root, text=f"{player1_name} = {Player1}", font=("Arial", 14), bg="lightyellow").grid(row=3, column=3)
    Label(root, text=f"{player2_name} = {Player2}", font=("Arial", 14), bg="lightyellow").grid(row=4, column=3)

# ===== Choose Player Symbol =====
def choose_player(symbol):
    global Player1, Player2, current_player
    Player1 = symbol
    Player2 = "O" if symbol == "X" else "X"
    current_player = Player1
    btn_X.destroy()
    btn_O.destroy()
    create_board()
    show_player_info()

# ===== Player 2 Name Input =====
def player2_input():
    global name_label2, name_entry2, next_btn2, welcome_label, name_label, name_entry, next_btn
    # Destroy Player 1 input widgets + Welcome Label
    welcome_label.destroy()
    name_label.destroy()
    name_entry.destroy()
    next_btn.destroy()
    
    # Player 2 input
    name_label2 = Label(root, text="Enter Player 2 Name:", font=("Arial", 16), bg="lightblue")
    name_label2.grid(row=0, column=0, padx=10, pady=20)

    name_entry2 = Entry(root, font=("Arial", 16))
    name_entry2.grid(row=0, column=1, padx=10, pady=20)

    def next_player2():
        global player2_name
        player2_name = name_entry2.get() or "Player2"
        name_label2.destroy()
        name_entry2.destroy()
        next_btn2.destroy()
        show_choice_buttons()

    next_btn2 = Button(root, text="Next", command=next_player2, bg="green", fg="white", font=("Arial", 14))
    next_btn2.grid(row=1, column=0, columnspan=2, pady=10)

# ===== Player 1 Name Input =====
def next_player1():
    global player1_name
    player1_name = name_entry.get() or "Player1"
    player2_input()

# ===== Show X/O Choice Buttons =====
def show_choice_buttons():
    global btn_X, btn_O
    btn_X = Button(root, text="Play as X", width=12, height=3, bg="blue", fg="white", font=("Arial", 14), command=lambda: choose_player("X"))
    btn_X.grid(row=0, column=0, padx=20, pady=50)

    btn_O = Button(root, text="Play as O", width=12, height=3, bg="red", fg="white", font=("Arial", 14), command=lambda: choose_player("O"))
    btn_O.grid(row=0, column=1, padx=20, pady=50)

# ===== End Game Buttons =====
def show_end_buttons():
    restart_btn = Button(root, text="Restart", width=12, height=2, bg="green", fg="white", font=("Arial", 14), command=restart_game)
    restart_btn.grid(row=8, column=0, pady=10)

    exit_btn = Button(root, text="Exit", width=12, height=2, bg="red", fg="white", font=("Arial", 14), command=exit_game)
    exit_btn.grid(row=8, column=1, pady=10)

# ===== Restart & Exit Functions =====
def restart_game():
    global play_board, buttons, current_player
    play_board = [["#"]*3 for _ in range(3)]
    buttons = [[None]*3 for _ in range(3)]
    current_player = Player1

    # Remove old board buttons and result labels
    for widget in root.winfo_children():
        if isinstance(widget, Button):
            if widget not in (btn_X, btn_O):
                widget.destroy()
        if isinstance(widget, Label):
            if "wins!" in str(widget.cget("text")) or "Draw" in str(widget.cget("text")):
                widget.destroy()

    create_board()

def exit_game():
    root.destroy()

#Player 1 Input and Next button
def start_name_input():
    global name_label, name_entry, next_btn, welcome_label
    welcome_label = Label(root, text="WELCOME TO TIC TAC TOE", font=("Arial", 20, "bold"), bg="lightblue")
    welcome_label.grid(row=0, column=0, columnspan=2, pady=20)

    name_label = Label(root, text="Enter Player 1 Name:", font=("Arial", 16), bg="lightblue")
    name_label.grid(row=1, column=0, padx=10, pady=10)

    name_entry = Entry(root, font=("Arial", 16))
    name_entry.grid(row=1, column=1, padx=10, pady=10)

    next_btn = Button(root, text="Next", command=next_player1, bg="green", fg="white", font=("Arial", 14))
    next_btn.grid(row=2, column=0, columnspan=2, pady=10)

#Root Window
root = Tk()
root.title("TIC TAC TOE")
root.geometry('450x550')
root.configure(bg="lightblue")

start_name_input()
root.mainloop()


