# date : 20240201
# file : test27_eh.py
# desc : 예외발생 처리

def add(x, y) :
    return x + y

def minus(x, y) :
    return x - y

def multi(x, y) :
    return x * y

def divde(x, y) :
    try :
        return x / y
    except ZeroDivisionError as e:
        print('[오! 류!] => 제 숫자는 0이 될수 없습니다!')
        return 0
    return x / y # ZeroDivisionError 발생 
    #return 0

def getOperands(): # 계산 할 수를 입력받음
     # 34. 을 넣었을대 예외 발생 Value Error 뜸
     try:
        a, b = map(int, input('두 수 입력(구분자 공백) > ').split())
        return a, b
     except ValueError as e:
         # print(e) # 정확환 예외 메세지 출력
         print('입력 예외 : 정수만 입력하세요')
         return 1, 1

while True:
    menu = input('메뉴입력(p[더하기], m[빼기], t[곱하기], d[나누기], x[exit] ?)')
    
    if menu == 'p':
        a, b = getOperands()
        print(f'덧셈 {a} + {b} = {add(a,b)}')
        # print(a,b)
        # print('더하기 처리')
    
    elif menu == 'm':
        a, b = getOperands()
        print(f'빼기 {a} - {b} = {minus(a,b)}')
        # print(a,b)
        # print("빼기")

    elif menu == 't':
        a, b = getOperands()
        print(f'곱하기 {a} * {b} = {multi(a,b)}')
        # print(a,b)
        # print("곱하기")
    
    elif menu == 'd':
        a, b = getOperands()
        print(f'나누기 {a} / {b} = {divde(a,b)}')
        # print(a,b)
        # print("나누기")
    
    elif menu == 'x':
        break

    else :
        continue # 다시 메뉴 선택으로 올라감