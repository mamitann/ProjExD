import tkinter as tk
import tkinter.messagebox as tkm


#練習3
def button_click(event):
    btn = event.widget
    num = btn["text"]
    if num == "x":
        num = "*"
    elif num == "÷":
        num = "/"
    elif num == "%":
        entry.insert(tk.END, float(num)/100)
    elif num == "+/-":
        entry.insert(tk.END, num*(-1))
    elif num == "AC":
        entry.delete(0, tk.END)

    
    if num == "=":
        #練習7
        siki = entry.get() #数式の文字列
        res = eval(siki)#数式文字の評価
        entry.delete(0, tk.END)#表示文字列の削除
        entry.insert(tk.END, res)#結果の挿入
    else:
        #tkm.showinfo("", f"{num}ボタンがクリックされました")
        #練習6
        entry.insert(tk.END, num)

#練習1
root = tk.Tk()
root.geometry("400x700")

#練習4
entry = tk.Entry(root, justify="right", width=10, font=("", 40))
entry.grid(row=0, column=0, columnspan=4)

#練習2
r, c =2, 0

for i in range(9, -1, -1):
    button = tk.Button(root, text=f"{i}", width=4, height=2, font=("", 30))
    button.grid(row= r, column= c)
    button.bind("<1>", button_click)
    c += 1
    if c%3 == 0:
        r += 1
        c = 0

#練習5
operators1 = ["AC", "+/-", "%", "÷"]
operators2 = ["x", "-", "+", "="]
r, c = 1, 0
for ope in operators1:
    button = tk.Button(root, text=f"{ope}", width=4, height=2, font=("", 30))
    button.grid(row=1, column=c)
    button.bind("<1>", button_click)
    c += 1
    if c == 3:
        r += 1

for ope in operators2:
    button = tk.Button(root, text=f"{ope}", width=4, height=2, font=("", 30))
    button.grid(row=r, column=3)
    button.bind("<1>", button_click)
    r += 1



root.mainloop()