import random


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
    @staticmethod
    def bmi(member):
        this = member
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
        self.com = myRandom(0, 2)

    def game(self):
        c = self.com
        u = self.user
        rps = ['가위', '바위', '보']
        b = c - u
        if b == 1 or b == -2:
            res = '컴퓨터 승리'
        elif b == 2 or b == -1:
            res = '사용자 승리'
        elif b == 0:
            res = '무승부'
        else:
            res = 'Wrong'
        return res


class Quiz09GetPrime(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def prime(self):
        res = ''


class Quiz10LeapYear(object):
    def __init__(self, year):
        self.year = year
    def leapYear(self):
        if(self.year % 4 == 0) & (self.year % 100 == 0) & (self.year % 400 == 0):
            res = '윤년입니다.'
        else:
            res = '평년입니다.'
        return res


class Quiz11NumberGolf(object):
    def __init__(self):
            pass


class Quiz12Lotto(object):
    @staticmethod
    def lottoNumber():
        lotto = random.sample(range(1, 46), 6) #지정한 숫자만큼의 요소들을 랜덤으로 뽑아 리스트로 반환
        lotto.sort() #오름차순으로 정렬
        return lotto

class Quiz13Bank(object):  # 이름, 입금, 출금만 구현
    def __init__(self):
            pass

class Quiz14Gugudan(object):  # 책받침구구단
    def __init__(self):
            pass


