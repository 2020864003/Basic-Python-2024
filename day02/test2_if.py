# date : 20240130
# desc : 여러조건 if문자

date = input('날짜 입력 (예: 12/31)')

month = date.split('/')[0] # '12'
day = date.split('/')[1] # '31'

if month == '12' and day == '25' : ## 12월 25일
    print('Merry Christmas')

elif month == '01' and day == '01' : ##1월 1일
    print('Happy New Year')

elif month == '04' and day == '14' :
    print('delicious')

else :
    print('Personal Day')