import pandas as pd

pd.options.mode.chained_assignment = None  # default='warn'


def condenseArray(df, position):
    """Finds the most frequent assignment group
    sets the value at position to \"default\"at all
    rules where the assignment is the most frequent value
    and removes all the duplicates"""
    # gets the most frequent value
    mostFreq = df.iloc[:, -1].value_counts().idxmax()

    # splits arrrays into most frequent array and the rest
    default = df[df.iloc[:, -1] == mostFreq]
    unique = df[df.iloc[:, -1] != mostFreq]

    # sets everything between position and the assignment to "default"
    default.at[:, position:-1] = "default"

    # drops all duplicates
    default = default.drop_duplicates()

    # returns default and unique dataframes
    return [default, unique]


def combineDataFrames(df1, df2):
    """Combines the two dataframes, returns none if neither dataframe
    has content"""
    if df1 is None and df2.empty:
        return df1
    if df1 is None:
        return df2
    newCombinedDF = pd.concat([df1, df2], ignore_index=True)
    return newCombinedDF


def recursiveCondense(df, position=0):
    """Main algorithm that splits the data or condenses the array
     if it hits the end or has only one unique group in the data set."""
    condensed = None
    unique = None

    if(df.iloc[:, -1].unique().shape[0] == 1):
        # condenses array if there is only 1 unique assignment group
        return condenseArray(df, position)

    elif(position == df.shape[1]-2):
        return condenseArray(df, position)
    else:
        # unique values to iterate through
        uniquePosValues = df.iloc[:, position].unique()

        for value in uniquePosValues:
            newdf = df[df.iloc[:, position] == value]

            [newCondensed, newUnique] = recursiveCondense(newdf, position+1)

            # combining data Frames
            condensed = combineDataFrames(condensed, newCondensed)

            unique = combineDataFrames(unique, newUnique)

        # condensing new condensed array
        [condensed, newUnique] = condenseArray(condensed, position)
        unique = combineDataFrames(unique, newUnique)

        # returning condensed and unique array
        return [condensed, unique]


def compress(df, position=0):
    """Main compression algorithm. Calls recursiveCondense
    and ten combines and returns the two data sets returned"""
    [condensedDF, uniqueDF] = recursiveCondense(df, position)
    return combineDataFrames(condensedDF, uniqueDF)
