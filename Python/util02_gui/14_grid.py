from tkinter import *

root = Tk()
root.title("오래노 GUI")
root.geometry("640x480+100+300")

# def btnquit():
#     root.quit()

# btn1 = Button(root,text="트로와버튼", command=btnquit)
# btn1.pack()

# btn2 = Button(root, text="버튼1")
# btn3 = Button(root, text="버튼2")

# # btn2.pack(side="left")
# # btn3.pack(side="right")

# btn2.grid(row=0,column=0)
# btn3.grid(row=1,column=1)

btn_f16 = Button(root, text="F16", width=5, height=2)
btn_f17 = Button(root, text="F17", width=5, height=2)
btn_f18 = Button(root, text="F18", width=5, height=2)
btn_f19 = Button(root, text="F19", width=5, height=2)

btn_f16.grid(row=0, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_f17.grid(row=0, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_f18.grid(row=0, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_f19.grid(row=0, column=3, sticky=N+E+W+S, padx=3, pady=3)

btn_clear = Button(root, text="clear", padx=10, pady=10)
btn_eqa = Button(root, text="=", padx=10, pady=10)
btn_div = Button(root, text="/", padx=10, pady=10)
btn_star = Button(root, text="*", padx=10, pady=10)

btn_clear.grid(row=1, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_eqa.grid(row=1, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_div.grid(row=1, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_star.grid(row=1, column=3, sticky=N+E+W+S, padx=3, pady=3)

btn_7 = Button(root, text="7", padx=10, pady=10)
btn_8 = Button(root, text="8", padx=10, pady=10)
btn_9 = Button(root, text="9", padx=10, pady=10)
btn_min = Button(root, text="-", padx=10, pady=10)

btn_7.grid(row=2, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_8.grid(row=2, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_9.grid(row=2, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_min.grid(row=2, column=3, sticky=N+E+W+S, padx=3, pady=3)

btn_4 = Button(root, text="4", padx=10, pady=10)
btn_5 = Button(root, text="5", padx=10, pady=10)
btn_6 = Button(root, text="6", padx=10, pady=10)
btn_plu = Button(root, text="+", padx=10, pady=10)

btn_4.grid(row=3, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_5.grid(row=3, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_6.grid(row=3, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_plu.grid(row=3, column=3, sticky=N+E+W+S, padx=3, pady=3)

btn_1 = Button(root, text="1", padx=10, pady=10)
btn_2 = Button(root, text="2", padx=10, pady=10)
btn_3 = Button(root, text="3", padx=10, pady=10)
btn_ent = Button(root, text="enter", padx=10, pady=20)

btn_1.grid(row=4, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_2.grid(row=4, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_3.grid(row=4, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_ent.grid(row=4, column=3, rowspan=2, sticky=N+E+W+S, padx=3, pady=3)

btn_0 = Button(root, text="0", padx=20, pady=10)
btn_com = Button(root, text=".", padx=10, pady=10)

btn_0.grid(row=5, column=0, columnspan=2, sticky=N+E+W+S, padx=3, pady=3)
btn_com.grid(row=5, column=2, sticky=N+E+W+S, padx=3, pady=3)

root.mainloop()
