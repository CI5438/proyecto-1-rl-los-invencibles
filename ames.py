import pandas as pd
import sys

def fix_missing_with_mode(df):
    """Fixes missing value from all columns using the mode.
    """
    return df.fillna(df.mode().iloc[0])

def only_rows_from_numeric_gte_column_value(df, column, value):
    """Remove from dataframe rows whose 'column' value is not >= 'value'
    """
    return df.loc[df[column] >= value]

def drop_column(df, column):
    """Drop from dataframe 'column'
    """
    try:
        df = df.drop(column, axis=1)
    except ValueError as err:
        print(err)

    return df

def only_rows_from_categorical_column_value(df, column, value):
    """Remove rows from dataframe.

    Remaining dataframe will have ONLY rows whose column 'column' 
    has value 'value'
    """
    return df.loc[df[column] == value]

def dummies(df):
    """Get dummies variables for categorical data.
    
    :param: dataframe
    :return: dataframe
    """
    return pd.get_dummies(df)

def read_file(filename):
    """Reads file and process it using panda dataframes.
    
    :param: name of the file
    :return: dataframe
    """

    try:
        df = pd.read_csv(filename)
        return df
    except:
        print("File couldn't be read")
        sys.exit(-1)

def init():
    df = read_file("ww2.amstat.org.txt")
    
    # a) Data cleaning
    df = only_rows_from_categorical_column_value(df, "Sale Condition", "Normal")
    df = only_rows_from_numeric_gte_column_value(df, "Gr Liv Area", 1500)
    
    # other operations
    df = drop_column(df, 'PID')
    df = drop_column(df, 'Order')
    df = fix_missing_with_mode(df)

    # b) Normalization of data
    
    # c) Data splitting
    # df_training, df_validation = get_samples(df)

    df = dummies(df)

if __name__ == '__main__':
    init()
