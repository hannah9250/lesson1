import tkinter as tk
def key_pressed(event): 
    label.config(text= "key pressed: " + event.char)
def mouse_pressed(event): 
    label.config(text = "mouse clicked")
root = tk.Tk()
root.title("event handler")
root.geometry("400x300")
label = tk.Label(root, text = "press a key or click the mouse", font = ("Arial", 15))
label.pack(pady = 100)
root.bind("<Key>", key_pressed)
root.bind("<Button-1>", mouse_pressed)
root.mainloop()