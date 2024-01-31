# date : 20240131
# file : test23_module.py
# desc : 모듈사용하기
import math

PI = 3.141592
radius = 5
print(f'원의 크기는 {radius * radius * PI}')

## print(math.pi)
print(f'정확한 원의 크기는 {radius * radius * math.pi}')

print(f'cos(0) = {math.cos(0)}')
print(2 ** 10)
print(math.pow(2, 10))
print(math.ceil(3.1))
print(math.floor(3.5))
print(round(3.5)) # 반올림(너무 사용하니까 MATH에 없음. 기본함수)

import math as m # 별명을 짓기
print(m.sin(2))

from math import pi, pow # 조심해서 사용해야함

print(pi)
print(pow(2, 10))