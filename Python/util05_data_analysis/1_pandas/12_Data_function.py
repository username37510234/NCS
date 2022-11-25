import pandas as pd
df = pd.read_excel('slam_score.xlsx', index_col='지원번호')

# df['키'] = df['키']+'cm' <- 이거 안댐

def add_cm(height):
    return str(height) + 'cm'

df['키'] = df['키'].apply(add_cm)

def capitialize(lang):
    if pd.notnull(lang):
        return lang.capitalize()
    return lang

df['SW특기'] = df['SW특기'].apply(capitialize)

print(df)