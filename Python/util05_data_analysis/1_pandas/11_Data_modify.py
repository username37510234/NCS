import pandas as pd
df = pd.read_excel('slam_score.xlsx', index_col='지원번호')

# print(df['학교'].replace({'북산고':'상북고','능남고':'무슨고'})) # 학교 column의 단어 바꾸기

# print(df['학교']+'등학교') # 문자 추가

df['총합'] = df['국어'] + df['영어'] + df['수학'] + df['과학'] + df['사회'] # 새로운 column 추가
df['평균'] = df['총합']/5
df['결과'] = 'Fail' # 결과 column 추가, 전부 Fail로
df.loc[df['평균']>80,'결과'] = 'Pass'  # 평균 80 이상인 항목의 결과를 Pass로
df.drop(columns=['총합'],inplace=True) # 총합 column 삭제

filt = df['수학']<80
# print(df.drop(index=df[filt].index)) # 필터 기준 인덱스를 구해서 제거

df.loc['9번'] = ['이정환','해남고',184,90,90,90,90,90,'Kotlin',90,'Pass']
df.loc['4번','SW특기'] = 'Python' # 4번 SW 특기를 Python으로
df.loc['5번',['키','SW특기']] = [189,'C']


cols = list(df.columns)
print(cols)

df = df[[cols[-1]]+ cols[0:-1]] # 맨 뒤에 있는 결과 colmun을 앞으로, 나머지 column과 합쳐 순서 변경

df.columns=['Result','이름', '학교', '키', '국어', '영어', '수학', '과학', '사회', 'SW특기', '평균']
print(df)