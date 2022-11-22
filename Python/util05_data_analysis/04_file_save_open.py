import pandas as pd

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

df.index.name = '지원번호'

# df.to_csv('slam_score.csv', encoding='utf-8-sig') # csv 파일로 저장

# df.to_csv('slam_score.txt', sep='\t', index=False) # txt 파일로 저장

# df.to_excel('slam_score.xlsx') # excel 파일로 저장

# df2 = pd.read_csv('slam_score.csv', skiprows=2) # csv 읽기
# skiprows = 지정 갯수 열을 건너 뜀
# df2 = pd.read_csv('slam_score.csv', skiprows=[1,3,5]) # [] 묶을시 해당 열 건너 뜀
# df2 = pd.read_csv('slam_score.csv', nrows=5) # 지정된 갯수 만큼만 가져옴

df2 = pd.read_csv('slam_score.txt', sep='\t') # txt 읽기

# df2= pd.read_excel('slam_score.xlsx')
print(df2)