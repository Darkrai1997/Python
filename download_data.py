# import webbrowser
# import urllib2
# webbrowser.open("http://www.baidu.com")
# page = urllib2.urlopen("http://www.baidu.com")
# contents = page.read()
# #获得了整个网页的内容也就是源代码
# print(contents)

#登陆
from selenium import webdriver
import time

#使用chormedriver
driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
#登陆网站
driver.get("https://cloud.sdsc.edu/v1/AUTH_sciviscontest/2004/isabeldata/")
time.sleep(1)
#获取地址
dow_pot = driver.find_elements_by_css_selector("a")
list=[]
for i in dow_pot:
    list.append(i.text)
#点击事件
def loop(k):
        for name in list[k:]:
            print(name)
            url = "https://cloud.sdsc.edu/v1/AUTH_sciviscontest/2004/isabeldata/" + name
            try:
                driver.get(url)
            except:
                time.sleep(3)
                pass
            #i.click()
            #k+=1
            time.sleep(60)
            continue


k=67
loop(k)