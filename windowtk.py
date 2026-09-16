import tkinter as tk
window = tk.Tk()
window.title("hi :)")
window.geometry("600x400")
label = tk.Label(window, text = "my name is hannah", font = ("Arial", 25))
label.pack()
window.mainloop()