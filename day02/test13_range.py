# date : 20240130
# file : test13_range.py
# desc : 복합자료형 딕셔너리

list_a = [1,2,3,4,5,6,7,8,9,10]
print(list_a)

# 범위 지정 range(n)
print(list_a)

# 범위 지정 range(n), 0개 -> n개의 범위 수를 생성
print(list(range(5)))
print(list(range(1,6))) # 1 ~ 5
print(list(range(2,21,2))) # 2 -> 20까지 2씩 증가
print(list(range(1,20,2))) # 1 -> 19까지 2씩 증가
print(list(range(10, -1, -1))) # countdown

# range() 클래스
list_a = list(range(1, 101))
print(list_a)

# 리스트 컨프리헨션
list_a = [
    i for i in range(1, 101)
]
print(list_a)