from sklearn.preprocessing import MinMaxScaler
import pandas as pd
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
import numpy as np


def Min_Max_normalization(Data):

    Data = Data.astype(float)
    # Create a MinMaxScaler object
    scaler = MinMaxScaler()

    # Fit and transform the data
    df_normalized = scaler.fit_transform(Data)

    # Convert the normalized array back to a dataframe
    df_normalized = pd.DataFrame(df_normalized, columns=Data.columns)

    return df_normalized


def value_restoration(Data):

    # Replace missing values with the mean (for numerical data) or median (for numerical data with outliers).
    imputer = IterativeImputer()

    df_imputed = imputer.fit_transform(Data)

    np.savetxt("Process.csv", df_imputed, delimiter=",", fmt="%d")

    return df_imputed


def Read_process(Input):

    # Data Normalization using min_max normalization
    # Data = Min_Max_normalization(Input)

    # Missing value restoration
    # Data = value_restoration(Data)

    print("\n.... Reading Pre_processed Data .....")

    Data = pd.read_csv("Process.csv", header=None)          # Pre_processed Data

    return Data
