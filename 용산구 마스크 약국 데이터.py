import requests  # OpenAPI 사용 시 필요

# 입력 주소에서 정보 가져오기
r = requests.get('https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByAddr/json?address=서울특별시 용산구')
# 가져온 정보를 파이썬이 사용할 수 있도록 변경
rjson = r.json()

# 상점 정보 꺼내기
store_list = rjson['stores']

# 상점 목록을 돌면서 작업 진행
for store in store_list:
    if store['remain_stat'] == 'plenty':  # 마스크가 충분한 양이 남아있는 약국이면
        print(store['addr'], store['name'])  # 약국의 주소, 이름 출력
