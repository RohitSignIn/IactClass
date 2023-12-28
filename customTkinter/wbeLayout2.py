import customtkinter

app = customtkinter.CTk()

app.geometry("800x600")
app.title("Web Layout")


app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)

# HEADER FRAME -- STARTS
headerFrame = customtkinter.CTkFrame(app, fg_color="#42d2dc", corner_radius=0)

headerFrame.grid(row = 0, column = 0, sticky="ewns")

headerFrame.grid_columnconfigure(0, weight=1)

# Header Label
headerLabel = customtkinter.CTkLabel(headerFrame, text="Header", font=("helvetica", 30, "bold"))
headerLabel.grid(row=0, column = 0, pady=70, sticky="ew")

# HEADER FRAME -- ENDS


wrapperFrame = customtkinter.CTkFrame(app, fg_color="red")
wrapperFrame.grid(row=1, column = 0, sticky="ewns")

wrapperFrame.grid_columnconfigure(0, weight=1)
wrapperFrame.grid_columnconfigure(1, weight=2)

# SIDE FRAME -- STARTS
sideFrame = customtkinter.CTkFrame(wrapperFrame, fg_color="#ffbd49", corner_radius=0)

sideFrame.grid(row = 0, column = 0, sticky="ewns")


# SIDE Label
sideLabel = customtkinter.CTkLabel(sideFrame, text="Side", font=("helvetica", 30, "bold"))
sideLabel.grid(row=1, column = 0, pady=100)

# SIDE FRAME -- ENDS

# CONTENT FRAME -- STARTS
contentFrame = customtkinter.CTkFrame(wrapperFrame, fg_color="#fe62b0", corner_radius=0)

contentFrame.grid(row = 0, column = 1, sticky="ewns")
contentFrame.grid_columnconfigure(0, weight=1)

# CONTENT Label
contentLabel = customtkinter.CTkLabel(contentFrame, text="Content", font=("helvetica", 30, "bold"))
contentLabel.grid(row=0, column = 0, pady=100)

# CONTENT FRAME -- ENDS


# FOOTER FRAME -- STARTS
footerFrame = customtkinter.CTkFrame(app, fg_color="#99e265", corner_radius=0)

footerFrame.grid(row = 2, column = 0, sticky="ew")


aFrame = customtkinter.CTkFrame(footerFrame, fg_color="red", corner_radius=0)

aFrame.grid(row = 0, column = 0, sticky="ew")

bFrame = customtkinter.CTkFrame(footerFrame, fg_color="blue", corner_radius=0)

bFrame.grid(row = 0, column = 1, sticky="ew")

cFrame = customtkinter.CTkFrame(footerFrame, fg_color="green", corner_radius=0)

cFrame.grid(row = 0, column = 2, sticky="ew")


footerFrame.grid_columnconfigure(0, weight=1)
footerFrame.grid_columnconfigure(1, weight=1)
footerFrame.grid_columnconfigure(2, weight=1)


# FOOTER FRAME -- ENDS

app.mainloop()