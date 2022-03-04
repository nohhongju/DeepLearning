import random

from hello import Member
from hello.domains import my100, myRandom, members, myMember


class Quiz00:
    def quiz00calculator(self) -> float:
        num1 = my100()
        op = ['+', '-', '*', '/', '%']
        num2 = my100()
        o = random.randint(0, 5)
        if op[o] == '+':
            res = num1 + num2
        elif op[o] == '-':
            res = num1 - num2
        elif op[o] == '*':
            res = num1 * num2
        elif op[o] == '/':
            res = num1 / num2
        elif op[o] == '%':
            res = num1 % num2
        print(f'{num1}{op[o]}{num2}={res:.2f}')
        return None

    def quiz01bmi(self):
        this = Member()
        this.name = myMember()
        this.height = myRandom(60, 220)
        this.weight = myRandom(10, 300)
        res = this.weight / (this.height * this.height) * 10000
        if res > 35:
            s = '고도비만'
        elif res > 30:
            s = '중(重)도 비만 (2단계 비만)'
        elif res > 25:
            s = '경도 비만 (1단계 비만)'
        elif res > 23:
            s = '과체중'
        elif res > 18.5:
            s = '정상'
        else:
            s = '저체중'
        print(f'이름: {this.name} 키: {this.height} 몸무게: {this.weight} BMI수치: {s}')
        return None

    def quiz02dice(self):
        res = myRandom(1, 6)
        print(f'{res}')
        return None

    def quiz03rps(self):
        user = myRandom(0, 2)
        com = myRandom(0, 2)
        rps = ['가위', '바위', '보']
        b = com - user
        if b == 1 or b == -2:
            res = f'유저: {rps[user]}, 컴퓨터: {rps[com]}, 컴퓨터 승리'
        elif b == 2 or b == -1:
            res = f'유저: {rps[user]}, 컴퓨터: {rps[com]}, 사용자 승리'
        elif b == 0:
            res = '무승부'
        else:
            res = 'Wrong'
        print(f'{res}')
        return None

    def quiz04leap(self):
        year = myRandom(0, 3000)
        if (year % 4 == 0) & (year % 100 == 0) & (year % 400 == 0):
            res = '윤년입니다.'
        else:
            res = '평년입니다.'
        print(f'{year}년은 {res}')
        return None

    def quiz05grade(self):
        kor = myRandom(0, 100)
        eng = myRandom(0, 100)
        math = myRandom(0, 100)
        sum = self.sum(kor, eng, math)
        avg = self.agv(kor, eng, math)
        grade = self.getGrade()
        passChk = self.passChk()
        return [sum, avg, grade, passChk]

    def sum(self):
        return self.kor + self.eng + self.math

    def avg(self):
        return self.kor + self.eng + self.math / 3

    def grade(self):
        pass

    def passChk(self):  # 60점이상이면 합격
        pass

    def quiz06memberChoice(self):

        return members[myRandom(0, 23)]

    def quiz07lotto(self):
        pass

    def quiz08bank(self):  # 이름, 입금, 출금만 구현
        pass

    def quiz09gugudan(self):  # 책받침구구단
        pass