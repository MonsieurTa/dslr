import pandas as pd
import numpy as np
import sys
import math
from tabulate import tabulate
from functools import reduce

class Describer:
  # type numpy.DataFrame
  df = None

  def __init__(self, filepath):
    self.df = pd.read_csv(filepath)

  # filter headers by float dtype
  def headers(self):
    return self.df.columns.values.tolist()[6:]

  def describe(self):
    data = {}
    for name in self.headers():
      values = cleaner(self.df, name)
      sortedvalues = np.sort(values)

      data.update({
        name: [
          count(values),
          mean(values),
          std(values),
          ft_min(values),
          percentile(sortedvalues, 25),
          percentile(sortedvalues, 50),
          percentile(sortedvalues, 75),
          ft_max(values),
        ],
      })
    index = ["count", "mean", "std", "min", "25%", "50%", "75%", "max"]
    return pd.DataFrame(data, index=index)

def cleaner(df, name):
  notnull = df[name].notnull()
  return df[notnull][name].values

def percentile(values, percentrank):
  if len(values) == 0:
    return np.nan

  x = (percentrank / 100)* (len(values) - 1)

  r = x % 1
  i = math.floor(x)
  return values[i] + r * (values[i + 1] - values[i])

def count(values):
  return len(values)

def mean(values):
  if len(values) == 0:
    return np.nan
  return sum(values) / len(values)

def std(values):
  if len(values) == 0:
    return np.nan
  return math.sqrt(sum((values - mean(values)) ** 2) / (len(values) - 1))

def ft_min(values):
  if len(values) == 0:
    return 0
  ret = values[0]
  for v in values:
    if v < ret:
      ret = v
  return ret

def ft_max(values):
  if len(values) == 0:
    return 0
  ret = values[0]
  for v in values:
    if v > ret:
      ret = v
  return ret

def normalize(values):
  amin = ft_min(values)
  amax = ft_max(values)
  return (values - amin) / (amax - amin)

def main():
  if len(sys.argv) > 1:
    d = Describer(sys.argv[1])

    print(d.describe())

if __name__ == "__main__":
  main()
