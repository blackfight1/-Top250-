#爬取如下
print("爬取豆瓣top250如下")
import requests
from bs4 import BeautifulSoup
headers = {
    "user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.1.5162 SLBChan/111"
}
for start_num in range(0, 250, 25):

    response = requests.get(f"https://movie.douban.com/top250?start={start_num}" ,headers = headers)
    html = response.text
    soup = (BeautifulSoup(html, "html.parser"))
    all_titles = soup.find_all("span", attrs={"class": "title"})
    for title in all_titles:
        title_string = title.string
        if "/" not in title_string:
            print(title_string)


