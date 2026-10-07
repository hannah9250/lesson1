from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
root = Tk()
root.title("DENOMINATION CALCULATOR")
root.configure(bg = "light blue")
root.geometry("650x450")
upload = Image.open("enemy.png")
upload = upload.resize(300,300)
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg="light blue")
labelplace = (x=180, y = 20)
label1 = Label(root, text= "Hello There, Welcome To The Denomination Calculator", bg="lightblue")
label1.place(relx=0.5, y=340, anchor= CENTER)
def msg(): 
    MsgBox = messagebox.showinfo(
        "alert"
        "Do you want to calculate the denomination count?"
    )
    if MsgBox =="ok": 
        topwin()
button1 = Button(
    root,
    text = "Lets Get Started!", 
    command=msg
    bg = "brown",
    fg = "white"
)
button1.place(x=260,y=360)
def Topwin(): 
    top = Toplevel()
    top.title("Denominations Calculator")
    top.configure(bg = "light grey")
    top.geometry("600x+350+50+50")
    label = Label(top, text = "enter the amount", bg ="lighgt grey")
    entry = Entry(top)
    lbl = Label(
        top,
        text = "Here are the number of notes for each denomination"
        bg = "light grey"
    )
    lbl.place(x=50, y=80)

    l1 = Label(top, text="2000", bg="light grey")
    l1.place(x=100, y=130)

    l2 = Label(top, text="500", bg="light grey")
    l2.place(x=100, y=170)

    l3 = Label(top, text="100", bg="light grey")
    l3.place(x=100, y=210)

    t1 = Entry(top)
    t1.place(x=180, y=130)

    t2 = Entry(top)
    t2.place(x=180, y=170)

    t3 = Entry(top)
    t3.place(x=180, y=210)


root.mainloop()
    

