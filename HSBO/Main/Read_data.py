# importing pandas library
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
from sklearn import preprocessing

# label_encoder object knows
# how to understand word labels.
label_encoder = preprocessing.LabelEncoder()


# ----------- Convert txt file into csv file -----------

def convert_file():
    # reading given csv file and creating dataframe
    dataframe1 = pd.read_csv("Dataset/KDDTrain+.txt")

    # storing this dataframe in a csv file
    dataframe1.to_csv('Dataset/KDDTrain+.csv', index=None)


def Process(Data):
    # String to number conversion

    Data[1] = label_encoder.fit_transform(Data[1])
    Data[2] = label_encoder.fit_transform(Data[2])
    Data[3] = label_encoder.fit_transform(Data[3])
    Data[41] = label_encoder.fit_transform(Data[41])

    return Data


def read_input():
    print("\n.... Reading input Network Traffic Data .....")

    Data = pd.read_csv("Dataset/KDDTrain+.csv", header=None)            # Network traffic data
    Data = Process(Data)

    return Data
