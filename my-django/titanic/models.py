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
        return pd.read_csv(this.context+this.fname)