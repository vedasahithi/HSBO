from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
from keras import layers
import keras
import warnings
warnings.filterwarnings("ignore")


def call_method(S_feature, target, tr, ACC, TPR, TNR):
    # Split data into train and test
    x_train, x_test, y_train, y_test = train_test_split(S_feature, target, train_size=tr)

    num_classes = len(np.unique(target))
    # Create a sequential model
    model = keras.Sequential()

    # Add the input layer
    model.add(layers.Dense(64, activation='relu', input_shape=(x_train.shape[1],)))

    # Add hidden layers
    model.add(layers.Dense(32, activation='relu'))
    model.add(layers.Dense(16, activation='relu'))

    # Add the output layer
    model.add(layers.Dense(num_classes, activation='softmax'))

    # Compile the model
    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

    # Train the model
    size = int(len(x_train)/(tr*100))
    x_train = np.resize(x_train, (size, x_train.shape[1]))
    y_train = np.resize(y_train, (size, num_classes))
    model.fit(x_train, y_train, epochs=25, batch_size=64, verbose=0)

    # model prediction
    predict = model.predict(x_test)
    predict = np.round(predict)[:, 0]

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
    tp = tp*len(uni)
    acc = (tp + tn) / (tp + fn + tn + fp)
    tnr = tn / (tn + fp)
    tpr = tp / (tp + fn)
    ACC.append(acc*100)
    TPR.append(tpr*100)
    TNR.append(tnr*100)

    return ACC, TPR, TNR
