import pandas as pd
# Compression Module
import assignmentCompression as compression


def main():
    """"""

    # get raw dataset
    df = pd.read_csv('./ExampleDataset.csv')

    # call the compression algorithm
    compressedDF = compression.compress(df)

    print(compressedDF.shape)

    # Save file results
    filename = input("What would you like to save this file as? :")
    compressedDF.to_csv('{}.csv'.format(filename), index=False)


if __name__ == '__main__':
    main()
