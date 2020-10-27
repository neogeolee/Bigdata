import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import re


#크롬 가상브라우저 실행
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')
browser = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)

keyword = "컴포즈커피"

url = 'https://www.instagram.com/explore/tags/{}/'.format(keyword)

instagram_tags = []

browser.get(url)
time.sleep(3)

browser.find_element_by_css_selector('div.v1Nh3.kIKUG._bz0w').click()
browser.find_element_by_css_selector('span.KPnG0').click()
time.sleep(3)

# 아이디, 비번 입력
input_id = browser.find_element_by_css_selector('#email')
input_pw = browser.find_element_by_css_selector('#pass')

input_id.send_keys('neogeolee@nate.com')
input_pw.send_keys('dlxognsdl1!')

#로그인 클릭
btn_submit = browser.find_element_by_css_selector('#loginbutton')
btn_submit.click()

time.sleep(10)
browser.find_element_by_css_selector('div.v1Nh3.kIKUG._bz0w').click()

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


browser.close()
browser.quit()
pd.DataFrame(instagram_tags).to_csv('compose.csv', encoding='utf-8')
