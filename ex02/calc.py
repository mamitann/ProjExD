import tkinter as tk

#練習1
root = tk.Tk()
root.geometry("300x500")

#練習2
r, c =0, 0

for i in range(9, -1, -1):
    button = tk.Button(root, text=f"{i}", width=4, height=2, font=("", 30))
    button.grid(row= r, column= c)
    c += 1
    if c%3 == 0:
        r += 1
        c = 0

root.mainloop()