import requests
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
import time
import csv
import codecs
import re
url='http://www.globalauthorid.com/WebPortal/EliteView?InfoID=996b3089-0a42-49a9-aeaa-38f67994cb3b'
brower=Chrome()
brower.get(url)
html=brower.page_source
#print(html)
content=brower.find_elements_by_xpath('//*[@id="ContentPlaceHolder1_ulAuthor"]/li/div[2]')
list=[]
for item in content:
    print(item.text)
    list.append(item.text)
#pattern='(.*?).*?机构：(.*?)ORCID:.*?论文数（\d+)'
#res=re.search(pattern,str(list))
#print(res)
da='//*[@id="ContentPlaceHolder1_pagerAll"]/a['
db=']'
for i in range(3,13):
    xpath=da+str(i)+db
    btn=brower.find_element_by_xpath(xpath)
#//*[@id="ContentPlaceHolder1_pagerAll"]/a[3]第二个按钮
#//*[@id="ContentPlaceHolder1_pagerAll"]/span  //*[@id="ContentPlaceHolder1_pagerAll"]/a[4]
    btn.click()#//*[@id="ContentPlaceHolder1_pagerAll"]/a[8]
    time.sleep(1)#//*[@id="ContentPlaceHolder1_pagerAll"]/span
    content=brower.find_elements_by_xpath('//*[@id="ContentPlaceHolder1_ulAuthor"]/li/div[2]')
    for item in content:
         print(item.text)#//*[@id="ContentPlaceHolder1_ulAuthor"]/li
         list.append(item.text)
print(list)
f = codecs.open('222.csv','w',encoding='utf-8')
writer = csv.writer(f)
for i in list:
    writer.writerow(i)


#with open('list123.csv', 'w', newline='', encoding='utf-8') as csvfile:
  #  writer = csv.writer(csvfile, delimiter='\n')
  #  writer.writerow(list)

#test_writer_data_1 = ['Tom', 'Cody', 'Zack']
#test_writer_data_2 = ['Mike', 'Bill']

#创建并打开文件
#with open('test_writer.csv', 'w', newline='', encoding='utf-8') as csvfile:
    #获得 writer对象 delimiter是分隔符 默认为 ","

    #writer = csv.writer(csvfile, delimiter=' ')
    #调用 writer的 writerow方法将 test_writer_data写入 test_writer.csv文件
    #writer.writerow(test_writer_data_1)
    #writer.writerow(test_writer_data_2)

#data = [
   # ("测试1",'软件测试工程师'),
    #("测试2",'软件测试工程师'),
    #("测试3",'软件测试工程师'),
    #("测试4",'软件测试工程师'),
    #("测试5",'软件测试工程师'),]
#f = open('222.csv','w')
#writer = csv.writer(f)
#for i in data:
 #   writer.writerow(i)
#f.close()



