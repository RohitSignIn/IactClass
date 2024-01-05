import customtkinter

app= customtkinter.CTk()

app.geometry("800x400")
app.title("Tic tac toe")

app.grid_rowconfigure(0,weight=1)
app.grid_columnconfigure(0,weight=1)

# def getiniticalstru():
#     return


# Frame tictactoe
ticToeTacframe = customtkinter.CTkFrame(app,width=100,height=400,fg_color="blue",corner_radius=0)
                        
ticToeTacframe.grid(row=0,column=0)    

# getiniticalstru()

app.mainloop()
                         

# layout - Buttons


