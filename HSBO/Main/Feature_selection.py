import pandas as pd
from sklearn.feature_selection import mutual_info_regression
from sklearn.svm import SVC
from sklearn.feature_selection import RFE
import warnings
warnings.filterwarnings("ignore")
import numpy as np
from Proposed_HSBOA_QRNN import HSBOA


def select_feature(Feature, target, N):

    # --------- SVM-RFE ---------
    # Create an SVM classifier
    estimator = SVC(kernel="linear")

    # Create the RFE object and fit it to the data
    selector = RFE(estimator, n_features_to_select=N, step=HSBOA.secretary_bird(10))
    selector = selector.fit(Feature, target)

    rank = selector.ranking_

    Feat_c = []
    for i in range(len(rank)):
        if rank[i] == 1:
            Feat_c.append(i)
    S_Feat1 = np.array(Feat_c)              # selected features using SVM-RFE method

    np.save("Selected_columns.npy", Feat_c)

    S_feat = []
    for i in range(len(S_Feat1)):
        Feat = Feature.iloc[:, S_Feat1[i]]
        S_feat.append(Feat)

    Selected_feat = np.array(S_feat).transpose()       # Selected Features
    # np.savetxt("S_Feature.csv", Selected_feat, delimiter=",", fmt="%s")


def feature_select(Feature, target, N):

    # Feature selection using SVM-RFE
    # select_feature(Feature, target, N)

    print("\n.... Reading Selected Features ....")

    S_feature = np.array(pd.read_csv("S_Feature.csv", header=None))

    return S_feature

