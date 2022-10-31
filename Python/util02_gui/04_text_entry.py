from tkinter import *

root = Tk()
root.title("오래노 GUI")
root.geometry("640x480+100+300")

def btnquit():
    root.quit()

btn1 = Button(root,text="트로와버튼", command=btnquit)
btn1.pack()

txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, "글자를 입력하세요")

e = Entry(root, width=30)
e.pack()
e.insert(0,"한 줄만 입력해요")

def btncmd():
    print(txt.get("1.0",END), end="") # 1= 첫번째 라인 : 0= 0번째 column 위치
    print(e.get(), end="")
    
    txt.delete("1.0",END)
    e.delete(0,END)
    
btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()