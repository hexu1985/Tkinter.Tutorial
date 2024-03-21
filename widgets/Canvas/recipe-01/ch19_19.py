# ch19_19.py
from tkinter import * 
import time
from random import * 

tk = Tk()
canvas = Canvas(tk,width=500, height=250)  # 建立画布
canvas.pack()
id1 = canvas.create_oval(10,50,60,100,fill="yellow")
id2 = canvas.create_oval(10,150,60,200,fill="aqua")

for x in range(0,100):
    if randint(1,100) > 70:
        canvas.move(id2,5,0) 
    else:
        canvas.move(id1,5,0)   # ID=1  x轴移动5像素，y轴移动2像素
    tk.update()          # 强制tkinter重绘
    time.sleep(0.05)

# tk.mainloop()

