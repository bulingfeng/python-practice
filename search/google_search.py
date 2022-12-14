import urllib
import requests
from bs4 import BeautifulSoup

query = "filetype pdf 英语4级"
# query = query.replace(' ', '+')
URL = f"https://google.com/search?q={query}"

# desktop user-agent
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
# mobile user-agent
MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"

headers = {"user-agent": MOBILE_USER_AGENT}
resp = requests.get(URL, headers=headers)

# 开始解析
results = []
if resp.status_code == 200:
    soup = BeautifulSoup(resp.content, "html.parser")
    print(soup.prettify())
    for g in soup.find_all('div', class_='r'):
        print(g)
        anchors = g.find_all('a')
        if anchors:
            link = anchors[0]['href']
            title = g.find('h3').text
            item = {
                "title": title,
                "link": link
            }
            results.append(item)
print(results)


# https://cloud.tencent.com/developer/article/1581779
# beautiful soup
# https://www.jianshu.com/p/424e037c5dd8