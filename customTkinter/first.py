import customtkinter

app = customtkinter.CTk()

app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)
button = customtkinter.CTkButton(app, text="ClickMe")
button.grid(row=0, column=0, padx=10, pady=10, sticky="ewns")

app.mainloop()