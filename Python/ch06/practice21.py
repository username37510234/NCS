from random import randrange


gun = 10


def checkpoint(soldier):
    global gun
    gun = gun - soldier
    print("[함수 내] 남은 총 : {0}".format(gun))


def checkpoint_ret(gun, soldier):
    gun = gun - soldier
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun


print("전체 총 : {0}".format(gun))
checkpoint(2)
print("남은 총 : {0}".format(gun))
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))


def std_weight(height, gender):
    if gender == "남자":
        height = height/100
        weight = round((height*height)*22,2)
        print("키 {0}cm {1}의 표준체중은 {2}kg입니다.".format(height*100,gender,weight))
    elif gender =="여자":
        height = height/100
        weight = round((height*height)*21,2)
        print("키 {0}cm {1}의 표준체중은 {2}kg입니다.".format(height*100,gender,weight))
    else:
        print("잘못된 입력입니다.")

std_weight(175,"남자")
std_weight(155,"여자")
sse = input("성별?")
std_weight(randrange(151,200),sse)
std_weight(randrange(151,200),sse)
std_weight(randrange(151,200),sse)
std_weight(randrange(151,200),sse)
std_weight(randrange(151,200),sse)
std_weight(randrange(151,200),sse)
std_weight(randrange(151,200),sse)
std_weight(randrange(151,200),sse)
std_weight(randrange(151,200),sse)
std_weight(randrange(151,200),sse)
std_weight(randrange(151,200),sse)
std_weight(randrange(151,200),sse)
std_weight(randrange(151,200),sse)
std_weight(randrange(151,200),sse)