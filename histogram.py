import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys
import describe

def most_homogeneous(d):
  headers = d.headers()
  cleaned = [ describe.cleaner(d.df, name) for name in headers ]
  normalized = [ describe.normalize(series) for series in cleaned ]
  stds = [ describe.std(v) for v in normalized ]
  minstd = describe.ft_min(stds)
  i = stds.index(minstd)
  return cleaned[i]

def main():
  if len(sys.argv) > 1:
    d = describe.Describer(sys.argv[1])
    data = most_homogeneous(d)

    plt.hist(data)
    plt.show()

if __name__ == '__main__':
  main()
