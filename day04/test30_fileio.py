# date : 20240201
# file : test30_fileio.py
# desc : Text 파일 읽기

fr = open('sample.txt', mode='r', encoding='utf-8')
fw = open('output.txt', mode='w', encoding='utf-8')

while True:
    line = fr.readline()
    if not line: 
        break # 조건문, 반복문 내의 코드가 한줄만 있으면 if 옆에 적을 수 있음
    print('내용', line.replace('\n', ''))
    fw.write(line)


fr.close()
fw.close()
