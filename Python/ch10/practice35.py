# langauge = input("무슨 언어를 좋아하세요?")
# print("{0}는 아주 좋은 언어입니다.".format(langauge))

# print(dir())
# import random
# print(dir())
# import pickle
# print(dir())

# print(dir(random))
# lst = [1,2,3]
# print(dir(lst))

# name = "Jim"
# print(dir(name))

# import glob
# print(glob.glob("*.py"))

# import os
# print(os.getcwd())

# folder = "sample_dir"

# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder,"폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder)
#     print(folder, "폴더를 생성하였습니다.")
# print(os.listdir())


# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime

# print("오늘 날짜는 ",datetime.date.today())

today = datetime.date.today()
td = datetime.timedelta(days=100)
print("우리가 만난지 100일은", today+td)

import byme
byme.sign()