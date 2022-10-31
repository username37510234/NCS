import time
from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title("오래노 GUI")
root.geometry("640x480+100+300")

def btnquit():
    root.quit()

btn1 = Button(root,text="트로와버튼", command=btnquit)
btn1.pack()

# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
progressbar.start(10)
progressbar.pack()

def btncmd():
    progressbar.stop()
    
btn = Button(root, text="클릭", command=btncmd)
btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1, 101):
        time.sleep(0.01)
        
        p_var2.set(i)
        progressbar2.update()
    
btn2 = Button(root, text="클릭", command=btncmd2)
btn2.pack()

root.mainloop()