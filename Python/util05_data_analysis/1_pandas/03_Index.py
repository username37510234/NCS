import pandas as pd

# lst = ['유재석','하하']
# print(lst[1])


data = {
    '이름' : ['채치수','정대만','송태섭','서태웅','강백호','변덕규','윤대협','황태산'],
    '학교' : ['북산고','북산고','북산고','북산고','북산고','능남고','능남고','능남고'],
    '키' : [197,184,168,187,188,202,190,188],
    '국어' : [90,40,80,40,15,80,100,55],
    '영어' : [85,35,75,60,20,100,85,65],
    '수학' : [100,50,70,70,10,95,90,45],
    '과학' : [95,55,80,75,35,85,95,40],
    '사회' : [85,25,75,80,10,80,95,35],
    'SW특기' : ['Python','Java','Javascript','','','C','PYTHON','C#']
}

df = pd.DataFrame(data, index=['1번','2번','3번','4번','5번','6번','7번','8번'])

# print(df.index)

# df.index.name = '지원번호'

# # print(df)

# df.reset_index(drop=True, inplace=True)

# print(df)

df.set_index('이름', inplace=True) # inplace 즉시 반영
df.sort_index(ascending=False, inplace=True)
print(df)