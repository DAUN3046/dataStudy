import requests

# 원하는 구 이름 저장
gus = ['용산구', '마포구', '종로구', '동작구']

# 구 이름마다 다음 내용을 반복
for gu in gus:
    place = '서울특별시 ' + gu # '서울특별시 용산구'와 같은 형식으로 이름 만들기
    # API 주소 만들기
    url = 'https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByAddr/json?address=' + place

    r = requests.get(url) # OpenAPI 정보 요청하기
    rjson = r.json()

    # 약국 정보 꺼내기
    store_list = rjson['stores']

    for store in store_list:
        try:
            if store['remain_stat'] == 'plenty': # 마스크의 양이 충분한 약국이면
                print(store['addr'] + ' - ' + store['name']) # 약국의 주소와 이름을 출력하기
        except: # 실행 중 에러가 발생할 경우 건너뜀
            continue