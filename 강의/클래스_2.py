class Employ:
    def __init__(self,name,career):
        self.name = name
        self.career = career
        print(self.name+"님의 연차는", str(self.career)+"입니다.")
    def salary(self):
        if self.career <= 5:
            self.salary = (self.career * 100) + 3000
        elif self.career <= 10:
            self.salary = (self.career * 110) + 3500
        elif self.career > 10:
            self.salary(self.career * 130) + 4000

        print("%s님의 연봉은 %d만원 입니다."%(self.name, self.salary))

    def degree(self):
        self.salary_d = int(self.salary) + 1000
        print("%s님의 연봉은 학위 소지로 인하여 %d만원 입니다."%(self.name,self.salary_d))
    def __getattr__(self,anything):
        print("잘못된 값입니다.")

a = Employ("파이썬", 7)

a.salary()

a.degree()

a.money

a.name, a.salary.d