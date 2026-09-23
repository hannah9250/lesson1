import tkinter as tk
root = tk.Tk()
root.title("number pad")
root.geometry("300x350")
frame = tk.Frame(root, relief = "ridge", borderwidth= 3)
frame.pack(pady = 30)
numbers = [
    ["1","2","3"],
    ["4","5","6"],
    ["7","8","9"],
    ["*","0","#"]
]
for row in range(4): 
    for column in range(3): 
        number = numbers[row][column]
        button = tk.Button(frame, text = number, width=5, height=2 )
        button.grid(row=row,column=column,pady= 5,padx = 5)
root.mainloop()