# date : 20240131
# file : test21_OOP.py
# desc : 클래스

# Class (사람이라는 객체를 만들기 위한 청사진) 만들기
class Person : # 사람 클래스 선언
    name = ' '
    age = 0
    gender = ''


    # 생성자 함수(스페셜 함수) => 클래스의 객체를 생성할때 동작.
    # init == initializtion(초기화)
    def __init__(self) -> None:
        self.name = 'Hong'
        self.age = 29
        self.gender = 'Man'

    # 클래스를 호출할때 원하는 형태로 변환해서 보여줄때
    def __str__(self) -> str:
        strs = f'custom 출력, 이름:{self.name} 객체 생성'
        return strs

    # memeber 함수
    def walk(self):
        print(f'{self.name}이(가) 걷습니다.')
    
    def stop(self):
       print(f'{self.name}이(가) 멈춥니다.')

# 사람 객체 생성 -> instance(사례, 예제)
roy = Person() # 함수 호출처럼 작성하면 됨
lee = Person()

# # print(type(roy))
# # print(type(3.14))
# # print(id(roy))
# # print(id(lee))


# 객체명.멤버변수
roy.name = '이정환'
roy.age = 28
roy.gender = '남자'

lee.name = '로이리'
lee.age = 27
lee.gender = '여자'

print(f'Roy => 이름:{roy.name} / 나이: {roy.age} / 성별: {roy.gender}')
print(f'Lee => 이름:{lee.name} / 나이: {lee.age} / 성별: {lee.gender}')

roy.walk()
print('1분동안 걷는다')
roy.stop()

lee.walk()
print('걷기 싫어함')
lee.stop()

print('생성자 함수 추가 함 -------------------------------->')

gd = Person()
print(f'gd => 이름:{gd.name} / 나이: {gd.age} / 성별: {gd.gender}')
print(gd)