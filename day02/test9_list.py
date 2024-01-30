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
print(list_1[2:3+1])
print(list_1[-1])
print(list_1[-5:-3])
print(list_1[4][2]) #[1,2,3,4] wnd 3만 가져 오기

list_2 = [[1,2,3],[4,5,6],[7,8,9]]
print(list_2[1],[2]) #6


## 리스트 연산 +, * 만 사용가능
list_3 = [4,5,6] # + 는 리스트 연결
list_4 = [7,8,9] # * 는 리스트 반복
list_5 = [1,2,3]

print(list_3 + list_4)
print((list_5 + list_3 + list_4) * 2)

#리스트 길이 함수 len()
print(len(list_1))
print(list_4[2])

## append() 리스트 마지막에 하나 추가
## insert(index, val) 리스트의 INDEX 이후에 VAL 추가
print(list_1)
list_1.append('Hello')

print(list_1)