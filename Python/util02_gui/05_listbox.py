from tkinter import *

root = Tk()
root.title("오래노 GUI")
root.geometry("640x480+100+300")

def btnquit():
    root.quit()

btn1 = Button(root,text="트로와버튼", command=btnquit)
btn1.pack()

listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()

def btncmd():
    # listbox.delete(END) # 맨뒤 삭제, 0을 넣으면 맨 앞 삭제
    
    # print("리스트에는",listbox.size(),"개가 있어요.")
    
    # print("1번째부터 3번째까지의 항목 : ", listbox.get(0,2))
    
    print("선택된 항목 : ", listbox.curselection())
    
btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()