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
html = sess.get('https://www.weather.go.kr/weather/observation/currentweather.jsp')

dom = bs(html.text, 'html.parser')

locals = dom.select('#content_weather > table > tbody > tr > td > a')
visibilities = dom.select('#content_weather > table > tbody > tr > td:nth-child(3)')
temps = dom.select('#content_weather > table > tbody > tr > td:nth-child(6)')
dews = dom.select('#content_weather > table > tbody > tr > td:nth-child(7)')
sens_temps = dom.select('#content_weather > table > tbody > tr > td:nth-child(8)')
precipitations = dom.select('#content_weather > table > tbody > tr > td:nth-child(9)')
humidities = dom.select('#content_weather > table > tbody > tr > td:nth-child(10)')
direction_winds = dom.select('#content_weather > table > tbody > tr > td:nth-child(11)')
sea_pressures = dom.select('#content_weather > table > tbody > tr > td:nth-child(13)')

# 파일로 저장 '20-07-15-16.csv'
fname = "{:%y-%m-%d-%H}.csv".format(datetime.now())
file = open(fname, mode='w', encoding='utf-8')

# csv 파일 헤더
file.write('지역, 시정, 현재기온, 이슬점온도, 체감온도, 일강수, 습도, 풍향, 해면기압\n')

for i in range(0, len(locals)):
    rs1 = locals[i].text
    rs2 = visibilities[i].text if visibilities[i].text.strip() else 'NA'
    rs3 = dews[i].text if dews[i].text.strip() else 'NA'
    rs4 = sens_temps[i].text if sens_temps[i].text.strip() else 'NA'
    rs5 = precipitations[i].text if precipitations[i].text.strip() else 'NA'
    rs6 = humidities[i].text if humidities[i].text.strip() else 'NA'
    rs7 = direction_winds[i].text if direction_winds[i].text.strip() else 'NA'
    rs8 = sea_pressures[i].text if sea_pressures[i].text.strip() else 'NA'

    file.write(rs1+','+
               rs2+','+
               rs3+','+
               rs4+','+
               rs5+','+
               rs6+','+
               rs7+','+
               rs8+'\n')
"""
print('지역 : ', local.text)
print('현재기온 : ', temp.text)
"""
# 파일 닫기
file.close()

# 브라우저 닫기
sess.close()