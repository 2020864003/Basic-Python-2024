# date : 20240130
# desc : if문 응용

import datetime

now = datetime.datetime.now()

if now.hour < 12 :
    print('AM')

if now.hour >= 12 :
    print('PM')