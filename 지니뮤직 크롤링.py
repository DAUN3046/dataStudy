import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML을 받아오기
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1', headers=headers)

# HTML을 BeautifulSoup이 검색하기 용이하도록 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서 tr들을 불러오기.
## tr들이 song number가 있음
## 해당 사이트의 content 속 newest-list 부분에 랭킹차트 있음.
songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

# movies(tr들)의 반복문 돌리기
for song in songs:
    #td 태그 중 클래스가 number인 녀석의 텍스트 중 0, 1번째 글자 가져오고 공백 제거
    ## td의 number 클래스는 순위를 가리킴
    rank = song.select_one('td.number').text[0:2].strip()
    #td 태그 중 클래스가 info인 녀석 바로 아래, 클래스가 title, ellipsis 중복으로 붙은 a 태그를 가져옴
    #a 태그의 텍스트 전부를 가져오고 좌우 공백 제거하기
    title = song.select_one('td.info > a.title.ellipsis').text.strip()
    #td태그 중 클래스가 info인 녀석 바로 아래, 클래스가 artist, ellipsis 중복으로 붙은 a 태그를 가져오기
    #a 태그의 텍스트 전부 가져오기
    artist = song.select_one('td.info > a.artist.ellipsis').text

    print(rank, title, artist)