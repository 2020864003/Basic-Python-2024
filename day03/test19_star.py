# date : 20240131
# file : test19_star.py
# desc : 별찍기 or 피라미드

# *
# **
# ***
# ****
# *****

for i in range(1, 5 + 1):
    # i 가 1이면, range(1,2) 1번 반복
    # i 가 2이면, range(1,3) 2번 반복

    for j in range(1, 6 - i + 1) :  # range() 값 바꿔서 디버깅
        print('*', end='') # enter 대신 empty
    print('') # 안쪽 for 문이 끝나면 엔터