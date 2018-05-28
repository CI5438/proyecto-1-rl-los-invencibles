import pandas as pd
import sys

def read_file(filename):
    """Reads file and process it using panda.
    
    :param: filename Name of the file
    """
    try:
        df = pd.read_csv(filename)
        return df
    except:
        print("Error al leer el archivo")
        sys.exit(-1)

def init():
    df = read_file("ww2.amstat.org.txt")

if __name__ == '__main__':
    init()
