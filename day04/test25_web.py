# date : 20240201
# file : test25_web.py
# desc : url library 모듈 사용법

# from urllib.request import * request 모듈 안의 모든 내용 다 사용 할 때
from urllib.request import Request, urlopen # Request클래스 와 urlopen 만 쓰겠다


req = Request('https://www.naver.com/') # 네이버 웹주소
res = urlopen(req) # url 주소로 웹사이트 열어달라고 요청

print(f' 응답코드는: {res.status}') # URL로 요청된 웹사이트 응답 확인!
print(res.read())


# urllib.request 보다 성능이 조금 더 나은 모듈
import requests

res2 = requests.get('https://www.naver.com/')

print(res2.status_code)
print(res2.text)