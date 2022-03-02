import random


def main():
    while 1:
        menu = input('0.Exit 1.계산기(+, -, *, /) 2.Bmi 3.Grade 4.GradeAuto 5.Dice 6. 7.RandomChoice 8.Rps 9. 10. 11. 12. 13. 14. ')
        if menu == '0':
            break
        elif menu == '1':  # 계산기
            q1 = Quiz01Calculator(int(input('첫번째 수')), input('연산자'), int(input('두번째 수')))
            print('*'*30+'\n' + f'{q1.num1}{q1.op}{q1.num2}= {q1.res()}')

        elif menu == '2':  # BMI
            q2 = Quiz02Bmi(input('이름: '), int(input('키: ')), int(input('몸무게: ')))
            print(f'이름: {q2.name}, 키: {q2.height}, 몸무게: {q2.weight}, BMI상태: {q2.bmi()}입니다.')

        elif menu == '3':  # 성적표
            q3 = Quiz03Grade(input('이름: '), int(input('국어: ')), int(input('영어: ')), int(input('수학: ')))
            print(f'이름: {q3.name}, 국어: {q3.kor}, 영어:{q3.eng}, 수학{q3.math}, 합계{q3.sum()}, 평균{q3.avg()}, 합격여부: {q3.chkPass()}')

        elif menu == '4':
            q4 = Quiz04GradeAuto()
            for i in ['국어', '영어', '수학']:
                print()

        elif menu == '5':
            print(Quiz05Dice.cast())

        elif menu == '6':
            q6 = None

        elif menu == '7':
            q7 = Quiz07RandomChoice()
            print(q7.chooseMember())

        elif menu == '8':
            q8 = Quiz08Rps(input('user: ')) # 가위 1 바위 2 보 3
            print(f'결과: {q8.game()}')

        elif menu == '9':
            q9 = Quiz09GetPrime(int(input('처음 숫자:')), int(input('마지막 숫자')))
            print(f'결과{q9.prime()}')

        elif menu == '10':
            q10 = None

        elif menu == '11':
            q11 = None

        elif menu == '12':
            q12 = None

        elif menu == '13':
            q13 = None

        elif menu == '14':
            q14 = None


class Quiz01Calculator:

    def __init__(self, num1, op, num2):
        self.num1 = num1
        self.op = op
        self.num2 = num2

    def res(self):
        if self.op == '+':
            return self.num1 + self.num2
        elif self.op == '-':
            return self.num1 - self.num2
        elif self.op == '*':
            return self.num1 * self.num2
        elif self.op == '/':
            return self.num1 / self.num2


class Quiz02Bmi:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def bmi(self):
        res = self.weight / (self.height * self.height) * 10000
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
        return s


class Quiz03Grade:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

    def sum(self):
        return self.kor + self.eng + self.math

    def avg(self):
        return self.sum() / 3

    def getGrade(self):
        pass

    def chkPass(self): # 60점이상이면 합격
        if self.avg() > 60:
            s = '합격'
        else:
            s = '불합격'
        return s


class Quiz04GradeAuto:
    def __init__(self, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math

    def sum(self):
        return self.kor + self.eng + self.math

    def avg(self):
        return self.sum() / 3

    def getGrade(self):
        pass

    def chkPass(self): # 60점이상이면 합격
        pass


def myRandom(start, end):
    return random.randint(start, end)


class Quiz05Dice:
    @staticmethod
    def cast():
        return myRandom(1, 6)


class Quiz07RandomChoice:
    def __init__(self):  # 803호에서 램덤으로 1명 이름 추출
        self.members = ['홍정명', '노홍주', '전종현', '정경준', '양정오',
                        "권혜민", "서성민", "조현국", "김한슬", "김진영",
                        '심민혜', '권솔이', '김지혜', '하진희', '최은아',
                        '최민서', '한성수', '김윤섭', '김승현',
                        '강 민', '최건일', '유재혁', '김아름', '장원종']
    def chooseMember(self):
        return self.members[myRandom(0, 23)]


class Quiz08Rps:
    def __init__(self, user):
        self.user = user
        self.com = myRandom(1, 3)

    def game(self):
        c = self.com
        u = self.user
        rps = ['가위', '바위', '보']
        if u == 1:
            if c == 1:
                res = '무승부'
            elif c == 2:
                res = '패배'
            elif c == 3:
                res = '승리'
        elif u == 2:
            if c == 1:
                res = '패배'
            elif c == 2:
                res = '무승부'
            elif c == 3:
                res = '승리'
        elif u == 3:
            if c == 1:
                res = '패배'
            elif c == 2:
                res = '승리'
            elif c == 3:
                res = '무승부'
        return res


class Quiz09GetPrime(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def prime(self,n):
        p = [False,False] + [True]*(n-1)
        for i in range(self.start, self.end+1):
            if p[i] == True:
                for j in range(2*i, n+1, i):
                    p[j] = False
        return p


class Quiz10LeapYear(object):
        def __init__(self):
            pass

class Quiz11NumberGolf(object):
        def __init__(self):
            pass

class Quiz12Lotto(object):
        def __init__(self):
            pass

class Quiz13Bank(object):  # 이름, 입금, 출금만 구현
        def __init__(self):
            pass

class Quiz14Gugudan(object):  # 책받침구구단
        def __init__(self):
            pass


if __name__ == '__main__':
    main()