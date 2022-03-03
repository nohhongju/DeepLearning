from titanic.views import View

if __name__ == '__main__':
    view = View()
    while 1:
        menu = input('1.전처리')
        if menu == '1':
            print(' ####1.전처리#### ')
            view.preprocess('train.csv', 'test.csv')
            break
        else:
            break