import requests
from bs4 import BeautifulSoup

url = "https://weather.naver.com/today/"

res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

today = soup.find("div",attrs={"class":"weather_area"})

sun = today.find("span",attrs={"class":"weather"}).get_text()
ondo = today.find("strong",attrs={"class":"current"}).get_text()
yester = today.find("span",attrs={"class":"temperature up"}).get_text()

print("{}, 어제보다 {}{}".format(sun, yester,ondo))
print()

res = requests.get("https://news.naver.com/")
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

bbs = soup.find_all("div",attrs={"class":"cjs_ctw"})
texts = soup.find_all("div",attrs={"class":"cjs_news_tw"})
broad = []
title = []
for bb in bbs:
     bbb = bb.find("h4",attrs={"class":"channel"}).get_text()
     broad.append(bbb)
     
for text in texts:
    ttt = text.find("div",attrs={"class":"cjs_t"}).get_text()
    title.append(ttt)
    
for i in range(0,5):
    print(broad[i],title[i])