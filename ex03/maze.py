import tkinter as tk
import maze_maker as mm
#import random 

def key_down(event):
    global key
    key = event.keysym

def key_up(evnet):
    global key
    key = ""

def print_clear():          #クリア画面表示
    root2 = tk.Tk()
    canvas2 = tk.Canvas(root2, width=500, height=500, bg="white")
    canvas2.pack()
    gameclear = tk.PhotoImage(file="fig/text_gameclear_j.png", master = root2)
    canvas2.create_image(250, 250, image=gameclear, tag="game_clear")

    root2.mainloop()

def main_proc():
    global cx, cy, mx, my, gameclear

    if (mx == 13 and my == 7):
        print_clear()

    if key == "Up": my -= 1
    if key == "Down": my += 1
    if key == "Left": mx -= 1
    if key == "Right": mx += 1
    if  maze_lst[mx][my] == 1:#移動先が壁だったら
        if key == "Up": my += 1
        if key == "Down": my -= 1
        if key == "Left": mx += 1
        if key == "Right": mx -= 1

    cx, cy = mx*100+50, my*100+50
    canvas.coords("kokaton", cx, cy)
    root.after(100, main_proc)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root, width=1500, height=900, bg="black")
    canvas.pack()

    maze_lst = mm.make_maze(15, 9)
    #print(maze_lst)
    mm.show_maze(canvas, maze_lst)
    
    kokaton = tk.PhotoImage(file="fig/8.png")
    
    mx, my = 1, 1
    cx, cy = mx*100+50, my*100+50
    sx, sy = 1, 1
    gx, gy = 13, 7

    gameclear = None
    
    canvas.create_oval(sx*100, sy*100, sx*100+100, sy*100+100, fill="green")  #スタートの追加
    canvas.create_oval(gx*100, gy*100, gx*100+100, gy*100+100, fill="red")  #ゴールの追加
    canvas.create_image(cx, cy, image=kokaton, tag="kokaton")

    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    main_proc()

    root.mainloop()
