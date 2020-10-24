import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys
from functools import reduce

import describe as dsc

def most_similar(d):
  headers = d.headers()
  cleaned_df = d.df.dropna()
  cleaned_data = [ cleaned_df[name] for name in headers ]
  normalized = [ dsc.normalize(series) for series in cleaned_data ]

  # min_spread = tuple = (value, feature_a, feature_b)
  # where value is the absolute diff between std(feature_a) and std(feature_b)
  # and feature_a and feature_b are column names
  min_spread = ()
  size = len(headers)
  i = 0
  while i < size:
    a_std = dsc.std(normalized[i])
    j = i + 1
    while j < size:
      b_std = dsc.std(normalized[j])

      abs_diff = np.abs(a_std - b_std)

      if min_spread == () or abs_diff < min_spread[0]:
        min_spread = (abs_diff, i, j)

      j += 1
    i += 1

  _, index_a, index_b = min_spread
  return cleaned_df, headers[index_a], headers[index_b]


def main():
  if len(sys.argv) > 1:
    d = dsc.Describer(sys.argv[1])

    cleaned_df, feature_a, feature_b = most_similar(d)

    groups = cleaned_df.groupby("Hogwarts House")
    for name, group in groups:
      plt.scatter(x=group[feature_a], y=group[feature_b], label=name)

    plt.xlabel(feature_a)
    plt.ylabel(feature_b)
    plt.legend()
    plt.show()

if __name__ == '__main__':
  main()
