from selenium import webdriver
from bs4 import BeautifulSoup
import time

# 브라우저 조절은 셀레니움의 option값 조절로
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

driver = webdriver.Chrome('c:\chromedriver.exe', options=options)

# 삼성전자, 네이버, SK텔레콤, SK이노베이션, 카카오
codes = ['005930', '035420', '017670', '096770', '035720']

for code in codes:
    url = 'https://m.stock.naver.com/item/main.nhn#/stocks/' + code + '/total'
    driver.get(url)
    time.sleep(2)
    
    soup = BeautifulSoup(driver.page_source, 'html.parser') # 가공

    name = soup.select_one('#header > div.end_header_topinfo > div.flick-container.major_info_wrp > div > div:nth-child(2) > div > div.item_wrp > div > h2').text
    current_price = soup.select_one('#header > div.end_header_topinfo > div.flick-container.major_info_wrp > div > div:nth-child(2) > div > div.stock_wrp > div.price_wrp > strong').text
    rate = soup.select_one('#header > div.end_header_topinfo > div.flick-container.major_info_wrp > div > div:nth-child(2) > div > div.stock_wrp > div.price_wrp > div > span.gap_rate > span.rate').text

    print(name, current_price, rate)

driver.quit()