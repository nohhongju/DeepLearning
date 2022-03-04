import random

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

class Quiz07RandomChoice:
    def __init__(self):  # 803호에서 램덤으로 1명 이름 추출
        self.members = ['홍정명', '노홍주', '전종현', '정경준', '양정오',
                        "권혜민", "서성민", "조현국", "김한슬", "김진영",
                        '심민혜', '권솔이', '김지혜', '하진희', '최은아',
                        '최민서', '한성수', '김윤섭', '김승현',
                        '강 민', '최건일', '유재혁', '김아름', '장원종']
    def chooseMember(self):
        return self.members[myRandom(0, 23)]


class Quiz09GetPrime(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def prime(self):
        res = ''

class Quiz12Lotto(object):
    @staticmethod
    def lottoNumber():
        lotto = random.sample(range(1, 46), 6) #지정한 숫자만큼의 요소들을 랜덤으로 뽑아 리스트로 반환
        lotto.sort() #오름차순으로 정렬
        return lotto



