import pandas as pd
import sys

def dummies(df):
    """Get dummies variables for categorical data
    
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
        print("Error al leer el archivo")
        sys.exit(-1)

def init():
    df = read_file("ww2.amstat.org.txt")
    df = dummies(df)

if __name__ == '__main__':
    init()
