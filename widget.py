import tkinter as tk
from datetime import date
window = tk.Tk()
window.title("my greet app")
window.geometry("600x450")
def greet_user():
    name = name_entry.get()
    today = date.today()
    message = "hello "+ name + "!\n"
    message += "todays date is " + str(today)+ "."
    output_text.delete("1.0", tk.END)
    output_text.insert("1.0", message)
label = tk.Label(window, text = "Enter your name: ")
label.pack()
name_entry = tk.Entry(window)
name_entry.pack()
button = tk.Button(window, text = "Greet Me", command = greet_user)
button.pack()
output_text = tk.Text(window, height = 5, width = 40)
output_text.pack()
window.mainloop()
