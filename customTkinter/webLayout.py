import customtkinter

app = customtkinter.CTk()

app.geometry("800x600")
app.title("Web Layout")


app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=2)
app.grid_rowconfigure(1, weight=1)

# HEADER FRAME -- STARTS
headerFrame = customtkinter.CTkFrame(app, fg_color="#42d2dc", corner_radius=0)

headerFrame.grid(row = 0, column = 0, sticky="ew", columnspan=2)

headerFrame.grid_columnconfigure(0, weight=1)

# Header Label
headerLabel = customtkinter.CTkLabel(headerFrame, text="Header", font=("helvetica", 30, "bold"))
headerLabel.grid(row=0, column = 0, pady=70)

# HEADER FRAME -- ENDS


# SIDE FRAME -- STARTS
sideFrame = customtkinter.CTkFrame(app, fg_color="#ffbd49", corner_radius=0)

sideFrame.grid(row = 1, column = 0, sticky="ewns")


# SIDE Label
sideLabel = customtkinter.CTkLabel(sideFrame, text="Side", font=("helvetica", 30, "bold"))
sideLabel.grid(row=0, column = 0, pady=100)

# SIDE FRAME -- ENDS

# CONTENT FRAME -- STARTS
contentFrame = customtkinter.CTkFrame(app, fg_color="#fe62b0", corner_radius=0)

contentFrame.grid(row = 1, column = 1, sticky="ewns")
contentFrame.grid_columnconfigure(0, weight=1)

# CONTENT Label
contentLabel = customtkinter.CTkLabel(contentFrame, text="Content", font=("helvetica", 30, "bold"))
contentLabel.grid(row=0, column = 0, pady=100)

# CONTENT FRAME -- ENDS


# FOOTER FRAME -- STARTS
footerFrame = customtkinter.CTkFrame(app, fg_color="#99e265", corner_radius=0)

footerFrame.grid(row = 2, column = 0, sticky="ew", columnspan=2)

footerFrame.grid_columnconfigure(0, weight=1)

# FOOTER Label
footerLabel = customtkinter.CTkLabel(footerFrame, text="Footer", font=("helvetica", 30, "bold"))
footerLabel.grid(row=0, column = 0, pady=70)

# FOOTER FRAME -- ENDS

app.mainloop()