import requests
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
import time
url='https://thurid.lib.tsinghua.edu.cn/scholar'
brower=Chrome()
#header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363'}
brower.get(url)
html=brower.page_source
print(html)
#content=brower.find_elements_by_xpath('/html/body/div[1]/div/div[5]/div[2]/div[1]/div[1]/div[2]')
da='//*[@id="scholarsImg"]/div['
db=']/a'
for i in range(1,10):
    xpath=da+str(i)+db
    btn=brower.find_element_by_xpath(xpath)
#//*[@id="ContentPlaceHolder1_pagerAll"]/a[3]第二个按钮
#//*[@id="ContentPlaceHolder1_pagerAll"]/span  //*[@id="ContentPlaceHolder1_pagerAll"]/a[4]
    btn.click()#//*[@id="ContentPlaceHolder1_pagerAll"]/a[8]
    time.sleep(1)#//*[@id="ContentPlaceHolder1_pagerAll"]/span
    content=brower.find_elements_by_xpath('/html/body/div[1]/div/div[5]/div[2]/div[1]/div[1]/div[2]')
    for item in content:
         print(item.text)
    btn1=brower.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[1]/a[2]')#//*[@id="ContentPlaceHolder1_ulAuthor"]/li
    btn1.click()
    time.sleep(1)