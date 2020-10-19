import pandas as pd
import numpy as np
import sys
from tabulate import tabulate
from functools import reduce

class Describer:
  # type numpy.DataFrame
  df = None

  def __init__(self, filepath):
    self.df = pd.read_csv(filepath)

  def header(self):
    def fn(row):
      _, dtype = row
      return np.issubdtype(dtype, float)
    def reducer(memo, v):
      return np.append(memo, v[0]) if fn(v) else memo
    return reduce(reducer, list(self.df.dtypes.iteritems()), np.array([]))

def main():
  if len(sys.argv) > 1:
    d = Describer(sys.argv[1])
    t = tabulate([[]], np.insert(d.header(), 0, ""))
    print(t)
if __name__ == "__main__":
  main()
