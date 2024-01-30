# date : 20240130
# desc : 흐름제어 if문자

## 조건이 참, 거짓일때 나누어서 어떠한 일처리 if
number = int(input('숫지 입력 >'))
## 입력 함수 input() = 문자
## int(input()) - 문자로 된 입력밧을 정수로 변겅

if number > 0 : ## if 조건:  참인 조건
    print('positive')

elif number == 0 : ## 양,음수 x
    print('0입니다~')

elif number < 0:
    print('negative')

else : ## else: 거짓인 조건
    print('정의 할수가 없습니다.')