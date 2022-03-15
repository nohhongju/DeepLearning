from titanic.domains import Dataset
import numpy as np
import pandas as pd
import sklearn

class Model:

    dataset = Dataset()

    def new_model(self, payload) -> object:
        this = self.dataset
        this.context = './data/'
        this.fname = payload
        # index_col=0 해야 기존 index 값이 유지된다.
        # 0은 컬럼명 중 첫번째를 의미한다(배열구조)
        return pd.read_csv(this.context+this.fname, index_col=0)
