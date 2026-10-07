import tkinter as tk

root = tk.Tk()
root.title("Workshop Greeting")
root.geometry("400x350")

tk.Label(root, text="Workshop Participant Greeting",
         font=("Arial", 18, "bold")).pack(pady=20)

tk.Label(root, text="Enter your name:").pack()
name = tk.Entry(root, width=30)
name.pack(pady=10)

output = tk.Text(root, height=7, width=40)
output.pack()

def check_in():
    output.delete("1.0", tk.END)
    output.insert(tk.END,
        f"Hello {name.get()}!\nWelcome to the workshop!\n"
        "Workshop Date: October 5, 2026")

tk.Button(root, text="Check In", command=check_in).pack(pady=10)

root.mainloop()
