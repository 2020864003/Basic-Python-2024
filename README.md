# Basic-Python-24
부경대학교 2024 IoT 개발자 과정 기초 프로그래밍 언어 － 파이썬


## 1일차 
- 개발환경 구축
    - 코딩폰트 - 나눔고딕코딩
    - Notepad++ 설치
    - Python 설치
    - Visual Studio Code 설치
    - Git 설치
        - TortoiseGit 설치
        - Github 가입
        - Github Desktop 설치


- 파이선 기초
    - 콘솔 출력
    - 주석
    - 변수
    - 자료형
    - 연산자


    ```python
    # 이 부분은 주석입니다.
    var01 = 10 # 정수, 실수, 불 , 문자열 모드 가능
    print(var10)
    print(type(var10))

    print(5 + 4 / 2) # 7.0
    print(5 == 4) # False
    ```
    
## 2일차
- 파이썬 기초
    - 흐름제어
        - if : 참/거짓으로 조건을 분기
        - for : 반복문 기본
        - while : 반복문 변형
    - 복합자료형 + 연산자(연산함수)
        - 리스트, 튜플, 딕셔너리
    - 출력 포맷
    - 구구단 + 디버깅

    ```python
    # debugging
    # F9(중단점 토글), F5(디버그시작), F10(한 줄씩 실행), F11(함수 안으로 진입)
    # Shift + F5(디버깅종료)    
    print('구구단 시작!')
    for x in range(2, 9+1): # 2부터 9까지 반복
        print(f'{x}단 ----------->')
    
        for y in range(1, 9+1): # 1부터 9까지 반복
            print (f'{x} x {y} = {x*y:2d}', end = '  ' ) # end= 엔터 대신 공백으로 변경
    print() # 안쪽 for문이 끝나면 마지막 엔터를 하나 추가


    ```

## 3일차
- 파이썬 기초
    - 입력 방법
    - 별찍기
    - 함수, 람다함수는 나중에~!...
    - 객체지향 OOP
        - 객체는 명사와 동사의 집합
        - 명사는 변수, 동사는 함수
        - 변수와 함수를 모두 모아 둔 곳 : 클래스(Class)
        - 클래스에서 하나씩 생성 : 객체(Object)