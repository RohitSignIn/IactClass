from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.title("Image Slider")

img1 = Image.open("./1.png").resize((400, 400))
img2 = Image.open("./2.png").resize((400, 400))
img3 = Image.open("./3.png").resize((400, 400))
img4 = Image.open("./4.jpg").resize((400, 400))
img5 = Image.open("./5.jpg").resize((400, 400))
img6 = Image.open("./6.jpg").resize((400, 400))

images = (
    img1,
    img2,
    img3,
    img4,
    img5,
    img6,
)

def showImage(indx):
    im = ImageTk.PhotoImage(images[indx])
    label = Label(root, image=im)
    label.image = im
    label.grid(row=0, column=0, columnspan=2)

showImage(0)

def handleNext(indx):
    global PrevBtn
    global NextBtn

    showImage(indx)

    if(indx == len(images)-1):
        NextBtn = Button(root, text="Next", state="disabled")

    PrevBtn = Button(root, text="Prev", command=lambda: handlePrev(indx-1))
    NextBtn = Button(root, text="Next", command=lambda: handleNext(indx+1))

    PrevBtn.grid(row=1, column=0)
    NextBtn.grid(row=1, column=1)

def handlePrev(indx):
    global PrevBtn
    global NextBtn

    showImage(indx)

    if(indx == 0):
        PrevBtn = Button(root, text="Prev", state="disabled")

    PrevBtn = Button(root, text="Prev", command=lambda: handlePrev(indx-1))
    NextBtn = Button(root, text="Next", command=lambda: handleNext(indx+1))

    PrevBtn.grid(row=1, column=0)
    NextBtn.grid(row=1, column=1)



PrevBtn = Button(root, text="Prev", state="disabled")
NextBtn = Button(root, text="Next", command=lambda: handleNext(1))

PrevBtn.grid(row=1, column=0)
NextBtn.grid(row=1, column=1)

root.mainloop()