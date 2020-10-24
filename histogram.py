import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys
from describe import Describer

def standardscore(v, mean, std):
  return (v - mean) / std

def main():
  if len(sys.argv) > 1:
    d = Describer(sys.argv[1])

    stds = [ d.std(d.notnull(name)) for name in d.headers() ]

    amin = np.amin(stds)

    print(amin)

if __name__ == '__main__':
  main()
