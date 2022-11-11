import requests
import re
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}

for i in range(1,7):
    url = "https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery=%EB%85%B8%ED%8A%B8%EB%B6%81&pagingIndex="+str(i)+"&pagingSize=10&query=%EB%85%B8%ED%8A%B8%EB%B6%81&viewType=thumb"

    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    items = soup.find_all(
        "li", attrs={"class": re.compile("^imgList_list_item__zYg0L")})

    for item in items:
        
        ad_badge = item.find("button", attrs={"class","ad_ad_stk__pBe5A"})
        if ad_badge:
            # print(" < 광고 상품 제외합니다 > ")
            continue
        name = item.find("a", attrs={"class": "imgList_link__fZgUG"}).get_text()
        price = item.find("span", attrs={"class": "price_num__S2p_v"}).get_text()

        review = item.find("em", attrs={"class": "imgList_num__ryhBm"})
        if review:
            review = review.get_text()
        else:
            # print(" < 리뷰 없는 상품 제외합니다 > ")
            continue
            
        if review == "999+":
            pass
        elif int(review) < 100:
            # print(" < 리뷰 수가 적어 제외합니다 >")
            continue
        
        if "Apple" in name:
            print(" < 애플이라 제외합니다 > ")
            continue
        
        print(f"제품명 {name}")
        print(f"가격 {price} 평가 {review}")
        print("-"*40)
    soup.clear()
