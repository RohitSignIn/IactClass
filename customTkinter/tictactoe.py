import customtkinter

app = customtkinter.CTk()

app.geometry("800x600")
app.title("Tic Tac Toe")

app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)

# GLOBAL 
playerTurn = "x"
movesDone = {} 
winner = False

def handleBtnClick(btnNum):
    global playerTurn


    # FORM NEW BUTTON
    btn = customtkinter.CTkButton(ticTacToeFrame, text=playerTurn, width=120, height=120, corner_radius=0, fg_color="#fff", text_color="#2d2d2d", hover_color="#fff", font=("helvetica", 68, "bold"))

    # SHOW NEW BUTTON
    if(btnNum >= 0 and btnNum < 3):
        btn.grid(row=0, column=btnNum, padx=5, pady=5)
    elif(btnNum >= 3 and btnNum < 6):
        btn.grid(row=1, column=abs(btnNum - 3), padx=5, pady=5)
    elif(btnNum >= 6 and btnNum < 9):
        btn.grid(row=2, column=abs(btnNum-6), padx=5, pady=5)

    movesDone[btnNum] = playerTurn
    checkWinner(playerTurn)

    # CHANGE PLAYER TURN
    if(playerTurn == "x"):
        playerTurn = "o"
    else:
        playerTurn = "x"

def checkWinner(playerTurn):
    global movesDone
    global winner 

    possibleWinnerCases = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6],
    ]

    for i in possibleWinnerCases:
        winner = True
        for j in i:
            if j in movesDone:
                if(movesDone[j] != playerTurn):
                    winner = False
                    break
            else:
                winner = False
                break
            
        if(winner):
            break

    if(winner):
        print("winner is ", playerTurn)
            


def getInitialStruc():
    btn0 = customtkinter.CTkButton(ticTacToeFrame, text="", width=120, height=120, corner_radius=0, fg_color="#fff", hover_color="#2d2d2d", command=lambda: handleBtnClick(0))
    btn1 = customtkinter.CTkButton(ticTacToeFrame, text="", width=120, height=120, corner_radius=0, fg_color="#fff", hover_color="#2d2d2d", command=lambda: handleBtnClick(1))
    btn2 = customtkinter.CTkButton(ticTacToeFrame, text="", width=120, height=120, corner_radius=0, fg_color="#fff", hover_color="#2d2d2d", command=lambda: handleBtnClick(2))

    btn3 = customtkinter.CTkButton(ticTacToeFrame, text="", width=120, height=120, corner_radius=0, fg_color="#fff", hover_color="#2d2d2d", command=lambda: handleBtnClick(3))
    btn4 = customtkinter.CTkButton(ticTacToeFrame, text="", width=120, height=120, corner_radius=0, fg_color="#fff", hover_color="#2d2d2d", command=lambda: handleBtnClick(4))
    btn5 = customtkinter.CTkButton(ticTacToeFrame, text="", width=120, height=120, corner_radius=0, fg_color="#fff", hover_color="#2d2d2d", command=lambda: handleBtnClick(5))
    
    btn6 = customtkinter.CTkButton(ticTacToeFrame, text="", width=120, height=120, corner_radius=0, fg_color="#fff", hover_color="#2d2d2d", command=lambda: handleBtnClick(6))
    btn7 = customtkinter.CTkButton(ticTacToeFrame, text="", width=120, height=120, corner_radius=0, fg_color="#fff", hover_color="#2d2d2d", command=lambda: handleBtnClick(7))
    btn8 = customtkinter.CTkButton(ticTacToeFrame, text="", width=120, height=120, corner_radius=0, fg_color="#fff", hover_color="#2d2d2d", command=lambda: handleBtnClick(8))

    btn0.grid(row=0, column=0, padx=5, pady=5)
    btn1.grid(row=0, column=1, padx=5, pady=5)
    btn2.grid(row=0, column=2, padx=5, pady=5)

    btn3.grid(row=1, column=0, padx=5, pady=5)
    btn4.grid(row=1, column=1, padx=5, pady=5)
    btn5.grid(row=1, column=2, padx=5, pady=5)

    btn6.grid(row=2, column=0, padx=5, pady=5)
    btn7.grid(row=2, column=1, padx=5, pady=5)
    btn8.grid(row=2, column=2, padx=5, pady=5)
    


ticTacToeFrame = customtkinter.CTkFrame(app, width=400, height=400,fg_color="transparent", corner_radius=0)
ticTacToeFrame.grid(row=0, column=0)

getInitialStruc()


app.mainloop()