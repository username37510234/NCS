sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)
print()

jumin = "990120-1234567"

print("성별 : "+jumin[7])
print("연 : "+jumin[0:2])
print("월 : "+jumin[2:4])
print("일 : "+jumin[4:6])

print("생년월일 : "+jumin[:6])
print("뒤 7자리 : "+jumin[7:])
print("뒤 7자리(뒤에부터) : "+jumin[-7:])
print()

python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))
print(python)

index = python.index("n")
print(index)
index = python.index("n", index+1)
print(index)

print(python.find("Java"))
# print(python.index("Java"))
print("hi")

print(python.count("n"))
print()

# print("a"+"b")
# print("a", "b")

print("나는 %d살입니다." % index)
print("나는 %s을 좋아해요." % "파이썬")
print("Apple 은 %c로 시작해요." % "A")

print("나는 %s살입니다." % 20)
print("나는 %s색과 %s색을 좋아해요" % ("파란", "빨간"))

print("나는 {}살입니다" .format(20))
print("나는 {}색과 {}색을 좋아해요" .format("빨간", "파란"))
print("나는 {0}색과 {1}색을 좋아해요" .format("빨간", "파란"))
print("나는 {1}색과 {0}색을 좋아해요" .format("빨간", "파란"))

print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨간", age=20))

age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요")
print("나는 %d살이며, %s색을 좋아해요" % (age, color))
print()

print("백문이 불여일견\n백견이 불여일타")

# print("저는 '나도코딩'입니다.")
# print('저는 "나도코딩"입니다.')
print("저는 \"나도코딩\"입니다.")

print("C:\\Users\\Nanocoding\\Desktop\\PythoWorkspace")

print("Red Apple\rPine")  # \r 커서를 맨 앞으로 이동시켜서 새로 쓰기

print("Redd\b Apple")

print("Red\t Apple")
print()


site = "http://naver.com"
site = site.replace("http://","")
site = site.replace(".com","")
eNum = str(site.count("e"))
moji = str(len(site))
site = site[:3]
password = site+moji+eNum+"!"

print("생성된 비밀번호 : %s"% password)