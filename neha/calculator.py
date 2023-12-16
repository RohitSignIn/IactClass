from tkinter import *
root = Tk()
entry = Entry(root, width=30)
entry.grid(row=0, column=0, columnspan=4)
a = Button(root, text = "9", width=5)
a.grid(row=1, column=0)
b = Button(root, text = "8", width=5)
b.grid(row=1, column=1)
c = Button(root, text = "7", width=5)
c.grid(row=1, column=2)
d = Button(root, text="+", width=5)
d.grid(row=1, column=3)
e = Button(root, text ="6", width=5)
e.grid(row=2, column=0)
f  = Button(root, text = "5", width=5)
f.grid(row=2, column=1)
g = Button(root, text = "4", width=5)
g.grid(row=2, column=2)
h = Button(root, text = "-", width=5)
h.grid(row=2, column=3) 
i = Button(root, text = "3", width=5)
i.grid(row=3, column=0)
j = Button(root, text = "2", width=5)
j.grid(row=3, column=1)
k = Button(root, text = "1", width=5)
k.grid(row=3, column=2)
l = Button(root, text = "*", width=5)
l.grid(row=3, column=3)

divZero = Button(root, text = "0", width=5)
divZero.grid(row=4, column=0)

divBtn = Button(root, text = "*", width=5)
divBtn.grid(row=4, column=1)

divClr = Button(root, text = "C", width=5)
divClr.grid(row=4, column=2)

divEql = Button(root, text = "=", width=5)
divEql.grid(row=4, column=3)



root.mainloop()