import os
# print(os.getcwd())
# os.chdir("Python/util04_rpa_basic")
# print(os.getcwd())
# os.chdir("..")
# print(os.getcwd())
# os.chdir("../..")
# print(os.getcwd())
# os.chdir("c:/NCS/Python/ch01")
# print(os.getcwd())

# file_path = os.path.join(os.getcwd(), "my_file.txt")
# # open("c:/NCS/img.png") as f ....

# print(file_path)

# print(os.path.dirname(r"C:\NCS\my_file.txt"))

import time
import datetime

# 생성일
ctime = os.path.getctime("file_menu.png")
print(ctime)
print(datetime.datetime.fromtimestamp(ctime).strftime("%Y년 %m월 %d일 %H:%M:%S"))

# 수정일
mtime = os.path.getmtime("file_menu.png")
print(datetime.datetime.fromtimestamp(mtime).strftime("%Y년 %m월 %d일 %H:%M:%S"))

file_path = "file_menu.png"

# 마지막 접근일
atime = os.path.getatime("file_menu.png")
print(datetime.datetime.fromtimestamp(atime).strftime("%Y년 %m월 %d일 %H:%M:%S"))

size = os.path.getsize(file_path)
print(size)