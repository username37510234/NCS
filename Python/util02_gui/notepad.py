import os
from tkinter import *


note = Tk()
note.title("제목 없음 - Windows 메모장")
note.geometry("640x480+100+300")

menubar = Menu(note)

file_name = "mynote.txt"

def fileopen():
    if os.path.isfile(file_name):
        with open(file_name,"r",encoding="utf-8") as file:
            txt.delete("1.0",END)
            txt.insert(END, file.read())
    
def filesave():
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(txt.get("1.0", END))

menubar_file = Menu(menubar, tearoff=0)
menubar_file.add_command(label="열기",command=fileopen)
menubar_file.add_command(label="저장",command=filesave)
menubar_file.add_command(label="끝내기",command=note.quit)
menubar.add_cascade(label="파일", menu=menubar_file)

menubar_edit = Menu(menubar, tearoff=0)
menubar.add_cascade(label="편집", menu=menubar_edit)

menubar_rule = Menu(menubar, tearoff=0)
menubar.add_cascade(label="서식", menu=menubar_rule)

menubar_view = Menu(menubar, tearoff=0)
menubar.add_cascade(label="보기", menu=menubar_view)

menubar_help = Menu(menubar, tearoff=0)
menubar.add_cascade(label="도움말", menu=menubar_help)

scrollbar = Scrollbar(note)
scrollbar.pack(side="right", fill="y")

txt = Text(note,yscrollcommand=scrollbar.set)
txt.pack(fill="both", expand=True)

scrollbar.config(command=txt.yview)

note.config(menu=menubar)
note.mainloop()