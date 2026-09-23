import tkinter as tk
from tkinter import messagebox
def scan(): 
    messagebox.showwarning("VIRUS DETECTED", "warning! a virus has been detected")
root = tk.Tk()
root.title("Virus Scanner")
root.geometry("400x300")
label = tk.Label(root,text = "virus scanner", font = ("Arial", 20))
label.pack(pady = 30)
button = tk.Button(root, text = "SCAN", command = scan)
button.pack(pady = 20)
root.mainloop()