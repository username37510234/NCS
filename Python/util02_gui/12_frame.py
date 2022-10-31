from ctypes import alignment
import time
import tkinter.messagebox as msgbox
from tkinter import *
from turtle import left

root = Tk()
root.title("오래노 GUI")
root.geometry("640x480+100+300")

def btnquit():
    root.quit()

btn1 = Button(root,text="트로와버튼", command=btnquit)
btn1.pack()

Label(root, text="메뉴를 선택해 주세요").pack(side="top")
Button(root, text="주문하기").pack(side="bottom")

frame_burger = Frame(root, relief="solid", bd=1)
frame_burger.pack(side="left",fill="both", expand=True)

Button(frame_burger, text="햄버거").pack()
Button(frame_burger, text="치즈버거").pack()
Button(frame_burger, text="치킨버거").pack()

frame_drink = LabelFrame(root, text="음료")
frame_drink.pack(side="right",fill="both",expand=False)
Button(frame_drink, text="콜라").pack()
Button(frame_drink, text="사이다").pack()
Button(frame_drink, text="우유").pack()
Button(frame_drink, text="물").pack()

frame_dessert = LabelFrame(root, text="뒤저트")
frame_dessert.pack(side="right",fill="both",expand=False)
Button(frame_dessert, text="감자튀김").pack()
Button(frame_dessert, text="빙수").pack()
Button(frame_dessert, text="아이스크림").pack()

root.mainloop()