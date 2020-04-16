#1초가 중요한 주식시장에서는 api사용, but 이 방법으로는 여러 사이트 응용 가능!

from selenium import webdriver
from bs4 import BeautifulSoup

import time

# 셀레니움 실행시 필요한 크롬드라이버 파일 가져오기
driver = webdriver.Chrome('C:\chromedriver.exe')

# 네이버 주식페이지 url 입력하기
url = 'https://m.stock.naver.com/item/main.nhn#/stocks/005930/total'

# 크롬으로 네이버 주식페이지에 접속
driver.get(url)

time.sleep(2) # 정보 받아오게 2초 기다리기

# 크롬에서 HTML 정보를 가져오고 BeautifulSoup를 통해 검색하기 쉽도록 가공하기
soup = BeautifulSoup(driver.page_source, 'html.parser')

name = soup.select_one('#header > div.end_header_topinfo > div.flick-container.major_info_wrp > div > div:nth-child(2) > div > div.item_wrp > div > h2').text
current_price = soup.select_one('#header > div.end_header_topinfo > div.flick-container.major_info_wrp > div > div:nth-child(2) > div > div.stock_wrp > div.price_wrp > strong').text
rate = soup.select_one('#header > div.end_header_topinfo > div.flick-container.major_info_wrp > div > div:nth-child(2) > div > div.stock_wrp > div.price_wrp > div > span.gap_rate > span.rate').text

print(name, current_price, rate)

# 크롬 종료
driver.quit()