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

# # 생성일
# ctime = os.path.getctime("file_menu.png")
# print(ctime)
# print(datetime.datetime.fromtimestamp(ctime).strftime("%Y년 %m월 %d일 %H:%M:%S"))

# # 수정일
# mtime = os.path.getmtime("file_menu.png")
# print(datetime.datetime.fromtimestamp(mtime).strftime("%Y년 %m월 %d일 %H:%M:%S"))

# file_path = "file_menu.png"

# # 마지막 접근일
# atime = os.path.getatime("file_menu.png")
# print(datetime.datetime.fromtimestamp(atime).strftime("%Y년 %m월 %d일 %H:%M:%S"))

# size = os.path.getsize(file_path)
# print(size)

# print(os.listdir())
# print(os.listdir("Python"))

# result = os.walk("Python")
# print(result)

# for root, dirs, files in result:
#     print(root, dirs, files)

# name = "11_file_system.py"
# result = []
# for root, dirs, files in os.walk("."):
#     if name in files:
#         result.append(os.path.join(root,name))
        
# print(result)

# import fnmatch
# pattern = "*.py"
# result = []
# for root, dirs, files in os.walk("."):
#     for name in files:
#         if fnmatch.fnmatch(name, pattern):
#             result.append(os.path.join(root,name))

# print(result)

# print(os.path.isdir("Python"))
# print(os.path.isfile("Python"))

# 파일생성
# open("new_file.txt","a").close()

# 이름바꾸기
# os.rename("new_file.txt","new_file_rename.txt")

# 삭제하기
# os.remove("new_file_rename.txt")

# 폴더생성
# os.mkdir("new_folder")

# os.makedirs("new_folders/a/b/c")

# os.rename("new_folder", "new_folder_rename")

# 삭제하기
# os.rmdir("new_folder_rename")
# os.removedirs("new_folders/a/b/c")

# import shutil
# shutil.rmtree("new_folders")

# shutil.copy("img.png","test_folder/copied_img.png")

# shutil.copyfile("img.png","test_folder/copied_img2.png")

# shutil.copy2("img.png","test_folder/copied_img3.png")

# copy, copyfile 메타 정보 복사 안함 / copy2 메타 정보 복사

# shutil.copytree("test_folder","testfolder2")

# shutil.move("test_folder","test_folder2")