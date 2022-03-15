from icecream import ic
from context.models import Model
from context.domains import Dataset


class TitanicModel(object):
    def __init__(self, train_fname, test_fname):
        self.model = Model()
        self.dataset = Dataset()
        self.train = self.model.new_model(train_fname)
        self.test = self.model.new_model(test_fname)
        # id 추출
        ic(f'트레인 컬럼{self.train.columns}')
        ic(f'트레인 헤드{self.test.head()}')
        ic(self.train)

    def preprocess(self):
        self.create_label()

    def create_label(self):
        pass