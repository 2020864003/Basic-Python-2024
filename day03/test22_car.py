# date : 20240131
# file : test22_car.py
# desc : car 클래스 만들기

class Car:
    wheel_num = 4
    color = 'white'
    plate_num = ' '
    company = ' '
    geartype= ' '


    # 전진, 후진, 좌회전, 우회전
    def moveForward(self):
        print(f'{self.plate_num}이 전진합니다.')

    def moveBackward(self):
            print(f'{self.plate_num}이 후진합니다.')

    def moveLeft(self):
        print(f'{self.plate_num}이 좌회전합니다.')

    def moveRight(self):
            print(f'{self.plate_num}이 우회전합니다.')
    
    # 생성자를 변경했으니까, 변경된 생성자로 호출
    def __init__(self, number, comp, col, gear) -> None:
           self.plate_num = number
           self.company = comp
           self.color = col
           self.geartype = gear

tucson = Car('12가 3456', 'HYUMDAI', 'BLACK','AUTOMATIC')
print(tucson)
print(f'차번호는 {tucson.plate_num}')
print(f'색상은 {tucson.color}')
tucson.moveForward()

ioniq = Car('98가7654', 'KIA', 'WHITE', 'MANUAL')
print(f'차번호는 {ioniq.plate_num}')