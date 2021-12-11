import sklearn.datasets as datasets
from sklearn.naive_bayes import GaussianNB as gnb
import pandas as pd

data = datasets.load_iris().data
target = datasets.load_iris().target

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

tab = pd.DataFrame(data,columns=datasets.load_iris().feature_names)
print(tab)

ptr = gnb()
ptr.fit(data,target)

print(datasets.load_iris().target_names[ptr.predict([[7.,3.2,4.7, 1.4]])])
