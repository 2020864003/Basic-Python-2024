# date : 20240131
# file : test21_OOP.py
# desc : 클래스

# Class (사람이라는 객체를 만들기 위한 청사진) 만들기
class Person : # 사람 클래스 선언
    name = ''
    age = 0
    gender = ''

# 사람 객체 생성 -> instance(사례, 예제)
roy = Person()
lee = Person()

# print(type(roy))
# print(type(3.14))
# print(id(roy))
# print(id(lee))

roy.name = '이정환'
roy.age = 28
roy.gender = '남자'

lee.name = '로이리'
lee.age = 27
lee.gender = '여자'

print(f'Roy => 이름:{roy.name} / 나이: {roy.age} / 성별: {roy.gender}')
print(f'Lee => 이름:{lee.name} / 나이: {lee.age} / 성별: {lee.gender}')