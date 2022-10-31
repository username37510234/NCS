import time
import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("오래노 GUI")
root.geometry("640x480+100+300")

def btnquit():
    root.quit()

btn1 = Button(root,text="트로와버튼", command=btnquit)
btn1.pack()

def info():
    msgbox.showinfo("알림","정상적으로 예매 완료되었습니다.")

def warn():
    msgbox.showwarning("경고","해당 좌석은 매진되었습니다.")

def error():
    msgbox.showerror("에러","결제 오류가 발생했습니다.")

def okcancel():
    msgbox.askokcancel("확인 / 취소","해당 좌석은 유아동반석입니다. 예매하시겠습니까?")

def retrycancel():
    response = msgbox.askretrycancel("재시도 / 취소", "일시적인 오류입니다. 다시 시도하겠습니까?")
    # print(response)
    if response == True:
        time.sleep(0.2)
        retrycancel()
    elif response == False:
        print("취소")

def yesno():
    msgbox.askyesno("예 / 아니오", "해당 좌석은 역방향입니다. 예매하시겠습니까?")

def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message="예매내역이 저장되지 않았습니다.\n저장 후 프로그램을 종료하시겠습니까?")
    # print(response)
    if response == True:
        print("저장되었습니다.")
        root.quit()
    elif response == False:
        print("저장되지 않았습니다.")
        root.quit()
    elif response == None:
        print("취소")

Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="에러").pack()
Button(root, command=okcancel, text="확인 취소").pack()
Button(root, command=retrycancel, text="재시도 취소").pack()
Button(root, command=yesno, text="예 아니오").pack()
Button(root, command=yesnocancel, text="예 아니오 취소").pack()


root.mainloop()