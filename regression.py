import pandas as pd

file = 'ex1data2.txt'
with open(file) as fh:
    data = fh.read()
print(data)