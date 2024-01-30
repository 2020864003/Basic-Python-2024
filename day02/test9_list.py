# date : 20240130
# desc : 복합자료형 list

## s1 = 100
## s2 = 80
## s3 = 90
## s4 = 10
## s5 = 70
## krsum = s1 + s2 + s3 + s4 + s5
## print(krsum)
## print(krsum/5)

# 총갯수 10(n) 면 인덱스 마지막 값 = 9(n-1)
#index = 0 , 1 , 2, 3, 4 , 5 , 6 , 7 , 8 , 9
std = [80,90,100,50,60,55,77,88,99,100]

print(std[9])


list_1 = [265, 3.4, '문자열', True, [1,2,3,4],(3,4), std]

print(list_1)
print(list_1[5])
list_1[6] = '바꾼값'
print(list_1)

## list 연산
print(list_1[2:4]) # : 뒤의 수는 추력하고 싶은 인덱스 + 1 이 필수
print(list_1[3])