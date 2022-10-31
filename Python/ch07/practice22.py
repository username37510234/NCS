print("Python","Java","JavaScirpt", sep=" vs ", end ="\t이었다...\n")
print("그랬다")

import sys
print("Python","Java", file=sys.stdout)
print("Python","Java", file=sys.stderr)

scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject,score, sep=" 과목은 ", end="점입니다.\n")
    print(subject.ljust(8), str(score).rjust(4), sep=":")
    
for num in range(1, 21):
    print("대기번호 : "+ str(num).zfill(3))
    
answer = input("아무 값이나 입력하세요 : ")
print(type(answer))
print("입력하신 값은 "+ answer + "입니다.")