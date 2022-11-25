import pandas as pd

temp = pd.Series([-20,-10,10,20])
print(temp)

print(temp[0],temp[2])

temp = pd.Series([-20,-10,10,20], index=['Jan','Feb','Mar','Apr'])

print(temp)

print(temp['Jan'],temp['Apr'])