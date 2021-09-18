class Car:
    def speedUp(self) : self.speed +=10 # 가속 동작 : 속도 10 증가
    def speedDown(self) : self.speed -=10 # 감속 동작 : 속도 10 감소
    def __init__(self, color, speed = 0):
        self.color = color
        self.speed = speed
car1 = Car('black', 0)
car2 = Car('red', 120)
car3 = Car('yellow', 30)
car4 = Car('blue', 0)
car5 = Car('green')

car2.speedDown() # car2 감속 : 속도 10 감소
car4.speedUp() # car4 가속 : 속도 10 증가
car3.color = 'purple' # car3의 색상을 purple로 변경
car5.speed = 100 # car5의 속도를 100으로 변경

class SuperCar(Car):
    def __init__(self, color, speed = 0, bTurbo = True):
        super().__init__(color,speed)
        self.bTurbo = bTurbo
    def setTurbo(self, bTurbo = True):
        self.bTurbo = bTurbo
    def speedUp(self):
        if self.bTurbo:
            self.speed += 50
        else:
            super().speedUp()
    def __str__(self):
        if self.bTurbo:
            return "[%s] [speed =%d] 터보모드" % (self.color,self.speed)
        else:
            return"[%s] [speed =%d] 일반모드" %(self.color, self.speed)


s1 = SuperCar("Gold", 0, True)
s2 = SuperCar("White", 0, False)
s1.speedUp()
s2.speedUp()
print("슈퍼카1:", s1)
print("슈퍼카2:", s2)
