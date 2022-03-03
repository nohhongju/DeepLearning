from hello.domains import Member
from hello.models import Quiz01Calculator, Quiz03Grade, Quiz04GradeAuto, Quiz05Dice, Quiz07RandomChoice, Quiz08Rps, \
    Quiz09GetPrime, Quiz02Bmi

if __name__ == '__main__':
    while 1:
        menu = input('0.Exit 1.계산기(+, -, *, /) 2.Bmi 3.Grade 4.GradeAuto 5.Dice 6. 7.RandomChoice 8.Rps 9. 10. 11. 12. 13. 14. ')
        if menu == '0':
            break
        elif menu == '1':  # 계산기
            q1 = Quiz01Calculator(int(input('첫번째 수')), input('연산자'), int(input('두번째 수')))
            print('*'*30+'\n' + f'{q1.num1}{q1.op}{q1.num2}= {q1.res()}')

        elif menu == '2':  # BMI
            member = Member()
            q2 = Quiz02Bmi
            q2.name = input('이름: ')
            q2.weight = float(input('키: '))
            q2.height = float(input('몸무게: '))
            res = q2.bmi(member)
            print(f'이름: {member.name}, 키: {member.height}, 몸무게: {member.weight}, BMI상태: {res}입니다.')

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