import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=799793"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
cartoons = soup.find_all("td", attrs={"class":"title"})
# title = cartoons[0].a.get_text()
# link = cartoons[0].a["href"]
# print(title, link)
# for idx, cartoon in enumerate(cartoons):
#     print(idx," "+cartoon.get_text())

ratings = soup.find_all("div", attrs={"class":"rating_type"})
dates = soup.find_all("td", attrs={"class":"num"})

totals = []

for cartoon in cartoons:
    title = cartoon.a.get_text()
    link = "http://comic.naver.com" + cartoon.a["href"]
    totals += title,link

for rating in ratings:
    rate = rating.find("strong").get_text()
    
for date in dates:
    update = date.get_text()


for total in totals:
    print(total)