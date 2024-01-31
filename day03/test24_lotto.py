# date : 20240131
# file : test24_lotto.py
# desc : lotto

import random as rnd # 랜덤은 주로 rnd로 줄여서 많이 사용

# numbers = list(range(1, 46))

# print(numbers)

# lottery = list()

# for i in range(6) : # 0,1,2,3,4,5 여섯번 반복
 #   lottery.append(rnd.choice(numbers))  # 1~45까지 숫자중 하나를 랜덤꺼내기 

# print(lottery.sort())
# print(lottery)

numbers = weight = list(range(1, 46))
lottery = list()
rnd.shuffle(weight) #가중치 섞음

lottery = rnd.choices(numbers, weights=weight, k=6) # 가중치로 한꺼번에 여섯개
lottery.sort()
print(lottery)