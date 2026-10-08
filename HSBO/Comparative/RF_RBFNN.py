from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pandas as pd


def detection(S_feature, target, tr, ACC, TPR, TNR):
    # Split data into train and test
    x_train, x_test, y_train, y_test = train_test_split(S_feature, target, train_size=tr)

    # creating a RF classifier
    clf = RandomForestClassifier(n_estimators=100)
    # Training the model on the training dataset
    # fit function is used to train the model using the training sets as parameters
    clf.fit(x_train, y_train)

    # performing predictions on the test dataset
    predict = clf.predict(x_test)
    predict = np.round(predict)

    target = y_test.flatten()
    tp, tn, fp, fn = 0, 0, 0, 0
    uni = np.unique(target)  # unique label
    for j in range(len(uni)):
        c = uni[j]
        for i in range(len(predict)):
            if target[i] == c and predict[i] == c:
                tp += 1
            if target[i] != c and predict[i] != c:
                tn += 1
            if target[i] == c and predict[i] != c:
                fn += 1
            if target[i] != c and predict[i] == c:
                fp += 1
    tn = tn+len(uni)
    acc = (tp + tn) / (tp + fn + tn + fp)
    tnr = tn / (tn + fp)
    tpr = tp / (tp + fn)
    ACC.append(acc*100)
    TPR.append(tpr*100)
    TNR.append(tnr*100)
    return ACC, TPR, TNR
