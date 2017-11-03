import pandas as pd
import assignmentCompression as compression


def main():
    input("\nGet Started? ")

    # get dataset
    df = pd.read_csv('./ExampleDataset.csv')

    compressedDF = compression.compress(df, 0)

    print(compressedDF.shape)

    # Save file results
    filename = input("What would you like to save this file as? :")
    compressedDF.to_csv('{}.csv'.format(filename),index=False)


if __name__ == '__main__':
    main()
