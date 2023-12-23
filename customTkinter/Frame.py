import customtkinter

app = customtkinter.CTk()

app.geometry("800x600")
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)

def homeLayout():
    mainLayout = customtkinter.CTkFrame(app, fg_color="red")
    mainLayout.grid(row=0, column=1, sticky="ewns")

def aboutLayout():
    mainLayout = customtkinter.CTkFrame(app, fg_color="blue")
    mainLayout.grid(row=0, column=1, sticky="ewns")

def contactLayout():
    mainLayout = customtkinter.CTkFrame(app, fg_color="green")
    mainLayout.grid(row=0, column=1, sticky="ewns")

# Side Bar
sideBar = customtkinter.CTkFrame(app, width=200, height=200, fg_color="#fff")

sideBar.grid(row=0, column=0, sticky="ns")

# Side Bar Buttons 
logo = customtkinter.CTkLabel(sideBar, text="Logo")

homeBtn = customtkinter.CTkButton(sideBar, text="Home", command=homeLayout)
aboutBtn = customtkinter.CTkButton(sideBar, text="About", command=aboutLayout)
contactBtn = customtkinter.CTkButton(sideBar, text="Contact", command=contactLayout)

# Show Side Bar Buttons
logo.grid(row=0, column=0, padx=5, pady=5)
homeBtn.grid(row=1, column=0, padx=5, pady=5)
aboutBtn.grid(row=2, column=0, padx=5, pady=5)
contactBtn.grid(row=3, column=0, padx=5, pady=5)

app.mainloop()