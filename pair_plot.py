import seaborn as sns
import matplotlib.pyplot as plt
import describe
import sys

def main():
  if len(sys.argv) > 1:
    d = describe.Describer(sys.argv[1])

    d.df.drop('Index', axis=1, inplace=True)
    d.df.dropna(inplace=True)

    sns.pairplot(d.df, markers='.', hue='Hogwarts House', diag_kind='hist')
    plt.show()

if __name__ == '__main__':
  main()
