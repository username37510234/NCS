from cProfile import label
from tkinter import *

root = Tk()
root.title("오래노 GUI")

def btnquit():
    root.quit()

btn1 = Button(root,text="트로와버튼", command=btnquit)
btn1.pack()

label1 = Label(root, text="안녕하세요.")
label1.pack()

photo = PhotoImage(file="Python/util02_gui/img_01.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="또 만나요.")
    
    global photo2
    photo2 = PhotoImage(file="Python/util02_gui/img_02.png")
    label2.config(image=photo2)

btn = Button(root, text="클릭", command=change)
btn.pack()

root.mainloop()