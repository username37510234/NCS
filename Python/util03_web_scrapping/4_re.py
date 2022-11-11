import re

p = re.compile("ca.e")
# . - 하나의 문자를 의미 > ca.e = case, cafe, care | caffe(X)
# ^ - 문자열의 시작 > ^de = desk, destiny, deny | lade(X)
# $ - 문자열의 끝 > (se$) = case, base, chase | security(X)


def print_match(m):
    # print(m.group()) # 매치되지 않으면 에러가 발생

    if m:
        print("m.group():", m.group())
        print("m.string:", m.string)
        print("m.start():", m.start())
        print("m.end():", m.end())
        print("m.sapn():", m.span())
    else:
        print("매칭되지 않음")

# m = p.match("careless")


m = p.search("good care")
# print_match(m)

lst = p.findall("careless")
print(lst)

# v = re.compile("원하는 형태")
# m = v.match("비교할 문자열") : 처음부터 일치하는 지 확인
# m = v.search("비교할 문자열") : 문자열에 일치하는 게 있는 지 확인
# lst = p.findall("비교할 문자열") : 일치하는 모든 것을 리스트 형태로 반환