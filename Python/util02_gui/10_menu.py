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

def create_new_file():
    print("새 파일을 만듭니다.")

menu = Menu(root)

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator()
menu_file.add_command(label="Open File...")
menu_file.add_separator()
menu_file.add_command(label="Save All", state="disable")
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=menu_file)

menu_edit = Menu(menu, tearoff=0)
menu_edit.add_command(label="Edit")
menu_edit.add_separator()
menu.add_cascade(label="Edit", menu=menu_edit)

menu_lang = Menu(menu, tearoff=0)
menu_lang.add_command(label="Python")
menu_lang.add_separator()
menu_lang.add_command(label="Java")
menu_lang.add_separator()
menu_lang.add_command(label="C++")
menu.add_cascade(label="Language", menu=menu_lang)

menu_view = Menu(menu, tearoff=0)
menu_view.add_command(label="Show Minimap")
menu_view.add_separator()
menu.add_cascade(label="View", menu=menu_view)

def btncmd():
    pass
    
btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.config(menu=menu)
root.mainloop()