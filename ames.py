import pandas as pd
import sys

def get_samples_DeCock(df, cols, force=True):
    """Return training and validation data samples using pandas's
    random sampling and Dean De Cock suggested method.

    De Cock states the following:

    "The two data sets can be easily created by randomizing the original data 
    and selecting the relevant proportion for each component with the only real
    requirement being that the number of observations in the training set be six 
    to ten times the number of variables."
    
    when force=True the training dataset lower limit is six times the number
    of variables (included), when false, the lower limit is the number
    of variables.

    NOTE: This function could be improved by relaxing the min_val_size within an 
    interval.
    """
    max_factor = 10
    min_factor = 6

    # calculate number of rows
    rows = len(df)

    # this algorithm begins trying with max factor and substracts one until
    # it finds the mentioned proportion of training/validation data.
    # Always makes sure validation data size is not less than 20% of the data.    
    factor = max_factor
    min_validation_size = round(rows/5)

    if min_validation_size == 0:
        # dont waste your time.
        raise ValueError("Dataset too small.")

    while (force and factor >= min_factor) or (factor > 0):
        training_size = cols*factor
        validation_size = rows - training_size
        
        if (validation_size >= min_validation_size):
            df_validation = df.sample(n=validation_size)
            df_training = df.sample(n=training_size)
            return df_training, df_validation
        else:
            factor -= 1
            continue
    
    raise ValueError("Dataset too small.")


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

def read_dataset(filename1, filename2):
    data_1 = []
    data_2 = []
    k = 0

    data_training = open(filename1, "r")
    data_validation = open(filename2, "r")

    for line in data_training:
        if k == 0:
            k+=1
            continue
        word = line.split(",")  
        data_1.append(word[1:])

    k = 0

    for line in data_validation:
        if k == 0:
            k+=1
            continue
        word = line.split(",")
        data_2.append(word[1:])
        
    print(len(columns[0]))
    for i in range(len(columns)):
        print(columns[i])

def norm(data1, data2):
    media=[1]
    varianza=[1]
    
    for i in range(1,len(data1[0])):
        aux=0
        for j in range(len(data1)):
            aux+=data1[j][i]

        for j in range(len(data2)):
            aux+=data2[j][i]
        
        media.append(aux/len(data1+data2))
    
    for i in range(1,len(data1[0])):
        aux=0
        for j in range(len(data1)):
            aux+=(data1[j][i]-media[i])**2

        for j in range(len(data2)):
            aux+=(data2[j][i]-media[i])**2
        varianza.append((aux/(len(data2+data1)-1))**(1/2))
    
    for i in range(1,len(data1[0])):
        for j in range(len(data1)):
            data1[j][i]=(data1[j][i]-media[i])/varianza[i]
        for j in range(len(data2)):
            data2[j][i]=(data2[j][i]-media[i])/varianza[i]

    return data1, data2

def init():
    df = read_file("ww2.amstat.org.txt")

    # a) Data cleaning
    df = only_rows_from_categorical_column_value(df, "Sale Condition", "Normal")
    df = only_rows_from_numeric_gte_column_value(df, "Gr Liv Area", 1500)
    
    # other operations
    df = drop_column(df, 'PID')
    df = drop_column(df, 'Order')
    df = fix_missing_with_mode(df)

    # calculate number of columns for sampling before getting dummies 
    # with dummies, there will be more variables so the sets would need
    # to be extremely large.
    cols = len(df.columns)
    
    df = dummies(df)

    # c) Data splitting
    df_training, df_validation = get_samples_DeCock(df, cols)

    # b) Data normalization
    df_training.to_csv("amstat_training.txt")
    df_validation.to_csv("amstat_validation.txt")
    
    
    # d) Model Assesing under training and validation data

    # criteria: bias -- average(yhat - y)

    # criteria: maximun deviation -- max(|y-yhat|)

    # criteria: mean absolute deviation -- average(|y-yhat|)

    # criteria: mean square error -- average(y-yhat)^2

if __name__ == '__main__':
    init()
