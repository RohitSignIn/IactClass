import customtkinter

app = customtkinter.CTk()


app.geometry("800x600")
app.title("App")
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=2)
app.grid_columnconfigure(1, weight=1)


# SideBar Frame 
sideBarFrame = customtkinter.CTkFrame(app, width=250, fg_color="#7b6ceb", corner_radius=0)

sideBarFrame.grid(row=0, column=0, sticky="ewns")



# Login frame
loginFrame = customtkinter.CTkFrame(app, width=250, fg_color="#fefefe", corner_radius=0)

loginFrame.grid_rowconfigure(0, weight=1)

loginFrame.grid(row=0, column=1, sticky="ewns")

loginInsideFrame = customtkinter.CTkFrame(loginFrame, width=250, bg_color="transparent", fg_color="transparent")
loginInsideFrame.grid(row=0, column=0)


# Form Widgets
label = customtkinter.CTkLabel(loginInsideFrame, text="USER LOGIN", padx=50, pady=15, font=("helvetica", 28, "bold"), text_color="#978fbe")

entry1 = customtkinter.CTkEntry(loginInsideFrame, border_width=0, fg_color="#eae6ff", width=200, text_color="#000")

entry2 = customtkinter.CTkEntry(loginInsideFrame, border_width=0, fg_color="#eae6ff", width=200, text_color="#000")

btn = customtkinter.CTkButton(loginInsideFrame, text="Submit", corner_radius=50, fg_color="#c96dc4", hover_color="#a06dda", font=("helvetica", 18, "bold"))


# Show Form Widgets
label.grid(row=0, column=0)
entry1.grid(row=1, column=0, pady=5)
entry2.grid(row=2, column=0, pady=5)
btn.grid(row=3, column=0, pady=10)


app.mainloop()