# date : 20240131
# file : test17_input.py
# desc : 콘솔 입력

# input()
# 출력 = com화면, 프린터, 스피커, 빔프로젝트. VR
# 입력 = 콘솔 입력(키보드), 마우스 입력, 목소리, 조이스틱. 터치 스크린
# input('내용 추가') -> 반드시 

temp_val = input('곱할 수 입력 >')
temp_val = int(temp_val) # 문자열 ->  정수형으로 change (형 변환)

print(f'입력 값 = {temp_val}')

# 곱하기
result = temp_val * 5
print(f'결과 = {result}')