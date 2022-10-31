from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title("오래노 GUI")
root.geometry("640x480+100+300")

def btnquit():
    root.quit()

btn1 = Button(root,text="트로와버튼", command=btnquit)
btn1.pack()

values = [str(i)+"일" for i in range(1,32)]
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("카드 결제일")

combobox_read = ttk.Combobox(root, height=5, values=values, state="readonly")
combobox_read.current(0)
combobox_read.pack()

def btncmd():
    print(combobox.get())
    print(combobox_read.get())
    
btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()