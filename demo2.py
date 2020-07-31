import requests
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
import time
url='http://www.globalauthorid.com/WebPortal/EliteView?InfoID=905a1ef0-4b67-4b55-91fb-7628aabebeba'
brower=Chrome()
brower.get(url)
html=brower.page_source
#print(html)
content=brower.find_elements_by_xpath('//*[@id="ContentPlaceHolder1_ulAuthor"]/li')
for item in content:
    print(item.text)
da='//*[@id="ContentPlaceHolder1_pagerAll"]/a['
db=']'
for i in range(3,10):
    xpath=da+str(i)+db
    btn=brower.find_element_by_xpath(xpath)
#//*[@id="ContentPlaceHolder1_pagerAll"]/a[3]第二个按钮
#//*[@id="ContentPlaceHolder1_pagerAll"]/span  //*[@id="ContentPlaceHolder1_pagerAll"]/a[4]
    btn.click()#//*[@id="ContentPlaceHolder1_pagerAll"]/a[8]
    time.sleep(1)#//*[@id="ContentPlaceHolder1_pagerAll"]/span
    content=brower.find_elements_by_xpath('//*[@id="ContentPlaceHolder1_ulAuthor"]/li')
    for item in content:
         print(item.text)#//*[@id="ContentPlaceHolder1_ulAuthor"]/li

