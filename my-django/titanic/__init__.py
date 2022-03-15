from titanic.models import TitanicModel
from titanic.views import TitanicView

if __name__ == '__main__':
    view = TitanicView()
    model = TitanicModel(train_fname='train.csv', test_fname='test.csv')
    while 1:
        menu = input('1.전처리')
        if menu == '1':
            print(' ####1.전처리#### ')
            # view.preprocess('train.csv', 'test.csv')
            break
        else:
            break