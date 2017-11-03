import pandas as pd
import numpy as np


def runQuery(tests, compressedDF):

    columns = list(compressedDF.columns.values)[:-1]

    i = -1
    while(True):

        # build query
        queryParts = ['{} == \"{}\"'.format(column,test) for column, test in zip(columns, tests)]
        results = compressedDF.query(' and '.join(queryParts))

        if(not results.empty):
            return results
        else:
            tests[i] = "default"
        i = i - 1


def test(rawDF, compressedDF, count=rawDF.shape[0]):
    wins = 0
    fails = 0

    perm = np.random.permutation(rawDF.shape[0])

    for i in perm[:count]:
        tests = list(rawDF.loc[i,:])[:-1]
        trueAssignment = list(rawDF.loc[i,:])[-1]

        results = runQuery(tests,compressedDF)

        if(results.iloc[:,-1].values == trueAssignment):
            wins = wins + 1
        else:
            fails = fails + 1

    return [wins, fails]


def main():
    # get dataset
    rawDF = pd.read_csv('./ExampleDataset.csv')
    # get compressed dataset
    compressedDF = pd.read_csv('./CompressedExampleDataset.csv')

    [wins, fails] = test(rawDF, compressedDF, 100)
    print('wins:{}'.format(wins))
    print('fails:{}'.format(fails))


if __name__ == '__main__':
    main()  
