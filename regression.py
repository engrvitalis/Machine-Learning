import pandas as pd
import numpy as np

file = 'ex1data2.txt'
with open(file) as fh:
    data = fh.read()
data = np.array(data)
print(data)