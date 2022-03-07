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
        y = myRandom(2000, 2022)
        '''
        s1 = "윤년" if y % 4 == 0 and y % 100 ! = 0 else "평년"
        s2 = "윤년" if y % 400 == 0 else "평년"
        Java style => String s = : () ? : ;
        s = (y % 4 == 0 && y % 100 != 0) ? "윤년" : (y % 400 == 0) ? "윤년" : "평년" ;
        Python Style  => s = "" if else ""
        s = "윤년" if y % 4 == 0 and y % 100 != 0 or y % 400 == 0 else "평년"
        '''
        if (y % 4 == 0) & (y % 100 == 0) & (y % 400 == 0):
            res = '윤년'
        else:
            res = '평년'
        print(f'{y}년은 {res}입니다.')
        return None

    def quiz05grade(self):
        name = myMember()
        kor = myRandom(0, 100)
        eng = myRandom(0, 100)
        math = myRandom(0, 100)
        sum = kor + eng + math
        avg = sum / 3
        passChk = "합격" if avg > 60 else "불합격"
        print(f'이름: {name}, 국어: {kor}, 영어: {eng}, 수학: {math}, 총점: {sum}, 평균: {avg: .2f}, 합격여부: {passChk}')
        return None


    def quiz06memberChoice(self):
        res = myMember()
        print(f'{res}')
        return None

    def quiz07lotto(self):
        lotto = random.sample(range(1, 46), 6)  # 지정한 숫자만큼의 요소들을 랜덤으로 뽑아 리스트로 반환
        lotto.sort()  # 오름차순으로 정렬
        print(f'{lotto}')
        return None

    def quiz08bank(self):  # 이름, 입금, 출금만 구현
        Account.main()

    def quiz09gugudan(self):  # 책받침구구단
        for k in range(2):
            for i in range(1, 10):
                for j in range(2, 6):
                    print(f'{j} * {i} = {i * j}', end='\t')
                print("")
            print("")
        return None


'''
08번 문제 해결을 위한 클래스는 다음과 같다.
[요구사항(RFP)]
은행이름은 비트은행
입금자 이름(name), 계좌번호(account_number), 금액(money) 속성값으로 계좌를 생성한다.
계좌번호는 3자리 - 2자리 - 6자리 형태로 랜덤하게 생성된다
예를 들면 123-12-123456 이다.
금액은 100~999만원 사이로 랜덤하게 입금된다. (단위는 만 단위로 암묵적으로 판단한다.)
'''
class Account(object):
    def __init__(self, name, account_number, money):
        self.BANK_NAME = '비트은행'
        self.name = myMember() if name == None else name
        # self.account_number = f'{myRandom(1, 999):0>3} - {myRandom(1, 99):0>2} - {myRandom(1, 999999):0>6}'
        self.account_number = self.creat_account_number() if account_number == None else account_number
        self.money = myRandom(100, 999) if money == None else money
    def to_string(self):
        return f'은행: {self.BANK_NAME}, ' \
               f'입금자: {self.name}, ' \
               f'계좌: {self.account_number}, ' \
               f'금액: {self.money}만원'

    def creat_account_number(self):
        '''
        ls = [str(myRandom(0, 9)) for i in range(3)]
        ls.append("-")
        ls += [str(myRandom(0, 9)) for i in range(2)]
        ls.append("-")
        ls += [str(myRandom(0, 9)) for i in range(6)]
        return "".join(ls)
        '''
        return "".join(['-'if i == 3 or i == 6 else str(myRandom(1, 9)) for i in range(13)])

    def del_account(self, ls, account_number):
        for i, j in enumerate(ls):
            if j.account_number == account_number:
                del ls[i]
    @staticmethod
    def main():
        ls = []
        while 1:
            menu = input('0.종료 1.계좌개설 2.계좌목록 3.입금 4.출금 5.계좌해지')
            if menu == '0':
                break
            elif menu == '1':
                acc = Account(None, None, None)
                print(f'{acc.to_string()}....개설되었습니다.')
                ls.append(acc)
            elif menu == '2':
                a = '\n'.join([i.to_string() for i in ls])
                print(a)
            elif menu == '3':
                account_number = input('입금할 계좌번호')
                deposit = input('입금액')
                for i, j in enumerate(ls):
                    if j.account_number == account_number:
                        pass

                #추가 코드 완성
            elif menu == '4':
                account_number = input('출금할 계좌번호')
                deposit = input('출금액')
                #추가 코드 완성
            elif menu == '5':
                account_number = input('탈퇴할 계좌번호')
            else:
                print('Wrong Number.. Try Again')
                continue