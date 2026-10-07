import tkinter as tk

root = tk.Tk()
root.title("ATM PIN Setup")
root.geometry("350x450")

frame = tk.Frame(root, bd=5, relief="raised")
frame.pack(pady=20)

tk.Label(frame, text="Account Number").grid(row=0, column=0)
account = tk.Entry(frame)
account.grid(row=0, column=1)

tk.Label(frame, text="PIN").grid(row=1, column=0)
pin = tk.Entry(frame, show="*")
pin.grid(row=1, column=1)

output = tk.Text(root, height=5, width=35)
output.pack()

def show():
    output.delete("1.0", tk.END)
    output.insert(tk.END, f"Account: {account.get()}\nPIN: {pin.get()}")

for i in range(1, 10):
    tk.Button(frame, text=i, command=lambda n=i: pin.insert(tk.END, n)).grid(
        row=(i+1)//3+1, column=(i-1)%3)

tk.Button(root, text="Submit", command=show).pack(pady=10)

root.mainloop()

