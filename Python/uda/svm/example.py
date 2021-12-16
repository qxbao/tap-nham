from sklearn import svm
import pandas as pd
import numpy as np
import math

ft = np.array([[-1,-1],[1,1]])
lb = np.array([0,1])

ptr = svm.SVC()
ptr.fit(ft,lb)

print(ptr.predict([[-1,0.4]]))
