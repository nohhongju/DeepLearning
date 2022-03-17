from icecream import ic
from context.models import Model
from context.domains import Dataset


class TitanicModel(object):
    model = Model()
    dataset = Dataset()
    def __init__(self, train_fname, test_fname):
        self.train = self.model.new_dframe(train_fname)
        self.test = self.model.new_dframe(test_fname)
        self.id = self.test['PassengerId']
        # id 추출
        # ic(f'트레인 컬럼{self.train.columns}')
        # ic(f'트레인 헤드{self.train.head()}')

    def preprocess(self):
        this = self.create_this(self.dataset)
        self.print_this(this)

        '''
        this = self.drop_feature(this)
        this = self.create_label(this)
        this = self.create_train(this)
        this = self.name_nominal(this)
        this = self.pclass_ordinal(this)
        this = self.sex_nominal(this)
        this = self.age_ratio(this)
        this = self.fare_ratio(this)
        this = self.embarked_nominal(this)'''
        return this

    @staticmethod
    def print_this(this):
        print('*' * 100)
        ic(f'1. Train 의 타입 : {type(this.train)}\n')
        ic(f'2. Train 의 컬럼 : {this.train.columns}\n')
        ic(f'3. Train 의 상위 1개 : {this.train.head(1)}\n')
        ic(f'4. Train 의 null의 개수 : {this.train.isnull().sum()}\n')
        ic(f'5. Test 의 타입 : {type(this.test)}\n')
        ic(f'6. Test 의 컬럼 : {this.test.columns}\n')
        ic(f'7. Test 의 상위 1개 : {this.test.head(1)}\n')
        ic(f'8. Test 의 null의 개수 : {this.test.isnull().sum()}\n')
        ic(f'9. ID 의 타입 : {type(this.id)}\n')
        ic(f'10. ID 의 상위 10개 : {this.id[:10]}\n')
        print('*' * 100)

    def create_this(self, dataset) -> object:
        this = dataset
        this.train = self.train
        this.test = self.test
        this.id = self.id
        return this

    @staticmethod
    def create_label(this) -> object:
        return this

    @staticmethod
    def create_train(this) -> object:
        return this

    def drop_feature(self, this) -> object:
        a = [i for i in []]
        '''
        self.sibSp_garbage(df)
        self.parch_garbage(df)
        self.ticket_garbage(df)
        self.cabin_ordinal(df)
        '''
        return this

    '''
        Categorical vs. Quantitative
        Cate -> nominal (이름) vs. ordinal (순서)
        Quan -> interval (상대) vs. ratio (절대)
    '''

    @staticmethod
    def pclass_ordinal(this) -> object:
        return this

    @staticmethod
    def name_nominal(this) -> object:
        return this

    @staticmethod
    def sex_nominal(this) -> object:
        return this

    @staticmethod
    def age_ratio(this) -> object:
        return this

    @staticmethod
    def fare_ratio(this) -> object:
        return this

    @staticmethod
    def embarked_nominal(this) -> object:
        return this








