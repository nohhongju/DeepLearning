class Calculator(object):

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def calc(self):
        pass

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        return self.num1 / self.num2

if __name__ == '__main__':
    while 1:
        menu = input('0.Exit 1.계산기(+, -, *, /)')
        if menu == '0':
            break
        elif menu == '1':
            num1 = int(input('첫번째 수'))
            opcode = input('연산자')
            num2 = int(input('두번째 수'))
            #객체생성
            calc = Calculator(num1, num2)
            print('*'*30)
            if opcode == '+':
                res = f'{calc.num1} + {calc.num2} = {calc.add()}'
            elif opcode == '-':
                res = f'{calc.num1} - {calc.num2} = {calc.sub()}'
            elif opcode == '*':
                res = f'{calc.num1} * {calc.num2} = {calc.mul()}'
            elif opcode == '/':
                res = f'{calc.num1} / {calc.num2} = {calc.div()}'
            print(res)




