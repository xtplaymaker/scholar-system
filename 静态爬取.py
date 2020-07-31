import requests
from bs4 import BeautifulSoup
url='https://www.whu.edu.cn/info/1183/3169.htm'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
resp=requests.get(url=url,headers=headers)
html=resp.content
#print(html)
bs=BeautifulSoup(html)
#print(bs)
result=bs.find_all('p')
#<div class="ini-box pr20 pt10"><i class="iconfont pr10"></i>机构：哈尔滨工业大学 机电工程学院 机器人研究所 教授</div>
for item in result:
    print(item.string)