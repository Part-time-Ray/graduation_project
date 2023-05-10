import requests
import json
from bs4 import BeautifulSoup
get_url = {}
urls = ['https://pttpedia.fandom.com/zh/wiki/%E5%88%86%E9%A1%9E:PTT%E6%B5%81%E8%A1%8C%E7%94%A8%E8%AA%9E',
       'https://pttpedia.fandom.com/zh/wiki/%E5%88%86%E9%A1%9E:PTT%E6%B5%81%E8%A1%8C%E7%94%A8%E8%AA%9E?from=%E5%AE%85%E5%AE%85%E7%9B%B8%E8%BC%95',
       'https://pttpedia.fandom.com/zh/wiki/%E5%88%86%E9%A1%9E:PTT%E6%B5%81%E8%A1%8C%E7%94%A8%E8%AA%9E?from=%E8%AA%AA%E5%80%8B%E7%AC%91%E8%A9%B1']
for url in urls:
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    a_tag = soup.find_all("a", class_="category-page__member-link")
    for data in a_tag:
        get_url[data['title']]='https://pttpedia.fandom.com' + data['href']
ans = {}
i=0
l=len(get_url)
for word in get_url:
    if i%3==0:
        print(str(i/l*100)[:5] + '%')
    i+=1
    resp = requests.get(get_url[word])
    soup = BeautifulSoup(resp.text, "html.parser")
    con = soup.find_all('meta', attrs={'name':'description'})
    if len(con)>=1:
        ans[word] = con[0]['content']
with open('test.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    