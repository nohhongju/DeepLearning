
from context.domains import Dataset
from context.models import Model
from titanic import TitanicModel
from icecream import ic
import matplotlib.pyplot as plt
'''
데이터 시각화
엔티티(개체)를 파트로 표현하는 것

모든 feature를 다 그려야 하지만, 시간 관계상
survived, pclass, sex, embarked 의 4개만 그린다.
템플릿 메소드 패턴으로 구성하시오
'''

class TitanicTemplate(object):
    model = Model()
    dataset = Dataset()
    def __init__(self, fname):
        self.entity = self.model.new_model(fname)
        this = self.entity
        ic(f'트레인의 타입: {type(this)}')
        ic(f'트레인의 컬럼: {this.columns}')
        ic(f'트레인의 상위5행: {this.head()}')
        ic(f'트레인의 하위5행: {this.tail()}')

    def visualize(self):
        this = self.entity
        self.draw_survived(this)
        self.draw_pclass(this)
        self.draw_sex(this)
        self.draw_embarked(this)

    @staticmethod
    def draw_survived(this) -> None:
        f, ax = plt.subplots(1, 2, figsize=(18, 8))
        this['Survived']
        plt.show()

    @staticmethod
    def draw_pclass(this) -> None:
        plt.show()

    @staticmethod
    def draw_sex(this) -> None:
        plt.show()

    @staticmethod
    def draw_embarked(this) -> None:
        plt.show()
