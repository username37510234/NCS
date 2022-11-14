menu = {"커피","우유","주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))

menu = str(menu)
print(menu, type(menu))

from random import *


first = randrange(1,21)
second = {randrange(1,21),randrange(1,21),randrange(1,21)}

print(" -- 당첨자 발표 -- ")
print("치킨 당첨자 : %d"%first)
print("커피 당첨자 : ",second)
print(" -- 축하합니다 --")

users = range(1,21)
users =list(users)

shuffle(users)

winners = sample(users, 4)

print(" -- 당첨자 발표 -- ")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print(" -- 축하합니다 --")
