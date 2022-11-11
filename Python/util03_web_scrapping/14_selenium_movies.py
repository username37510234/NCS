import requests
from bs4 import BeautifulSoup

url = "https://movie.daum.net/ranking/boxoffice/yearly?date=2019"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={"class":"item_poster"})
print(len(movies))

# with open("movie.html","w",encoding="UTF-8") as f:
#     f.write(soup.prettify())

for movie in movies:
    title = movie.find("a",attrs={"class":"link_txt"}).get_text()
    
    crowds = movie.find("span",attrs={"class":"txt_info"}).get_text()
    
    print(title, crowds)
    # soup.find_next_sibling