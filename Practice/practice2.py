import requests
from selenium import webdriver as wd
import pandas as pd
import time
import re

keyword = "컴포즈커피"

url = "https://www.instagram.com/explore/tags/{}/".format(keyword)

instagram_tags = []

driver = wd.Chrome("./chromedriver.exe")
driver.get(url)
time.sleep(3)

driver.find_element_by_css_selector('div.v1Nh3.kIKUG._bz0w').click()
driver.find_element_by_css_selector('span.KPnG0').click()
time.sleep(3)

# 아이디, 비번 입력
input_id = driver.find_element_by_css_selector('#email')
input_pw = driver.find_element_by_css_selector('#pass')

input_id.send_keys('neogeolee@nate.com')
input_pw.send_keys('dlxognsdl1!')

#로그인 클릭
btn_submit = driver.find_element_by_css_selector('#loginbutton')
btn_submit.click()

time.sleep(10)
driver.find_element_by_css_selector('div.v1Nh3.kIKUG._bz0w').click()

while True:
    try:
        for i in range(501):
            time.sleep(1)
            data = driver.find_element_by_css_selector('.C7I1f.X7jCj') # C7I1f X7jCj
            tag_raw = data.text
            tags = re.findall('#[A-Za-z0-9가-힣]+', tag_raw)
            tag = ''.join(tags).replace("#"," ") # "#" 제거

            tag_data = tag.split()

            for tag_one in tag_data:
                instagram_tags.append(tag_one)

            print(instagram_tags)

            driver.find_element_by_css_selector('a._65Bje.coreSpriteRightPaginationArrow').click()

            time.sleep(3)
    except:
        break


driver.close()
driver.quit()
pd.DataFrame(instagram_tags).to_csv('compose.csv', encoding='utf-8')
