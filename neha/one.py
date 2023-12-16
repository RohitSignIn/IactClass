from tkinter import *
def handlebtnclick():
    label = Label(root, text = "hlo")
    label.pack()
root = Tk()
label = Label(root, text = "email")
label.pack()
emaile = Entry(root)
emaile.pack()
label = Label(root, text = "password")
label.pack()
passe = Entry(root)
passe.pack()
btn = Button(root, text = "submit", command = handlebtnclick)
btn.pack()
emaile.insert(0, "enter email")
passe.insert(0, "enter password")
root.mainloop()

from tkinter import *
entry = Entry(root)
entry.grid(row=0, column=0)