import requests
url = "http://nadocoding.tistory.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
print("응답코드 :",res.status_code)

print(len(res.text))
# print(res.text)

with open("oraeno.html", "w",encoding="utf-8") as f:
    f.write(res.text)