"""
    날짜 : 2020/07/15
    이름 : 이태훈
    내용 : 날씨정보 크롤링
"""
import requests as req
from datetime import datetime
from bs4 import BeautifulSoup as bs
from selenium import webdriver

"""
# 가상 웹 실행
browser = webdriver.Chrome('./chromedriver.exe')

# 기상청 이동
browser.get('https://www.weather.go.kr/w/weather/now.do')

# 파싱
local = browser.find_element_by_css_selector('#sfc-city-weather > div.cont-box02 > div > div.cont02 > div > table > tbody > tr:nth-child(1) > td:nth-child(1) > a')
temp = browser.find_element_by_css_selector('#sfc-city-weather > div.cont-box02 > div > div.cont02 > div > table > tbody > tr:nth-child(1) > td:nth-child(6)')

print('지역 : ', local.text)
print('현재기온 : ', temp.text)
"""

# 세션시작
sess = req.session()

# 날씨 데이터 요청
html = sess.get('https://www.koreabaseball.com/Record/Player/HitterBasic/Basic1.aspx')

dom = bs(html.text, 'html.parser')

locals = dom.select('#cphContents_cphContents_cphContents_udpContent > div.record_result > table')

# 파일로 저장 '20-07-15-16.csv'
fname = "{:%y-%m-%d-%H}.csv".format(datetime.now())
file = open(fname, mode='w', encoding='utf-8')

# csv 파일 헤더
file.write('지역\n')

for i in range(0, len(locals)):
    rs1 = locals[i].text


    file.write(rs1+','+'\n')
"""
print('지역 : ', local.text)
print('현재기온 : ', temp.text)
"""
# 파일 닫기
file.close()

# 브라우저 닫기
sess.close()