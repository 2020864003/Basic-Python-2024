# date : 20240201
# file : test28_fileio.py
# desc : Text 파일 입출력

# mode : a(append = 내용 추가), r(read = 파일 읽기), w(write = 파일 쓰기)
# encoding : cp949(한글), utf - 8(만국 공통어)

f = open('sample.txt', mode= 'w', encoding='UTF-8')
# ............ 뭔가를 한다.
# write() 에서 엔터를 추가 할려면 마지막에 \n 추가하기
f.write('안녕하세요. 우리는 IoT 개발자 과정입니다. \n') # mode = a, w
f.write('NICE TO MEET YOU \n')

f.close() # 파일은 무조건 마지막에 닫는다
print('파일이 생성되었습니다.')