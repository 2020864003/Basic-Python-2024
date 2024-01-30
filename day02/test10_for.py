# date : 20240130
# desc : for 반복문

std = [80,90,100,50,60,55,77,88,99,100, 23]
kr_sum = 0

for i in std: #std 리스트에 값을 하나씩 i에 넣어서 반복할 요소가 있을때 까지
    kr_sum = kr_sum + i

print(kr_sum)
print(kr_sum / len(std)) # 리스트의 길이로 처리하면 소스를 다시 수정할 필요x
print(len(std))


list_a = [[1,3,5],[2,4,8],[10,15,20]]

for in_list in list_a:
    print(in_list)


for in_list in list_a:
    for item in in_list:
        print(item)