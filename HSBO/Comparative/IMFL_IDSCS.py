from sklearn.model_selection import train_test_split
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv1D, MaxPooling1D, Flatten, Dense


def detection(S_feature, target, tr, ACC, TPR, TNR):
    # Split data into train and test
    x_train, x_test, y_train, y_test = train_test_split(S_feature, target, train_size=tr)

    maxlen = (x_train.shape[1])*5
    # num_classes
    n_class = len(np.unique(target))
    # Define the model
    model = Sequential()

    # Add a 1D Convolutional layer
    model.add(Conv1D(filters=64, kernel_size=3, activation='relu', input_shape=(maxlen, 1)))

    # Add a MaxPooling layer
    model.add(MaxPooling1D(pool_size=2))

    # Add another Convolutional layer
    model.add(Conv1D(filters=128, kernel_size=3, activation='relu'))

    # Add another MaxPooling layer
    model.add(MaxPooling1D(pool_size=2))

    # Flatten the output of the previous layer
    model.add(Flatten())

    # Add a fully connected (Dense) layer
    model.add(Dense(64, activation='relu'))

    # Output layer for binary classification
    model.add(Dense(n_class, activation='sigmoid'))
    # Compile the model
    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

    # Train the model
    xt = int(len(x_train)/(tr*100))
    x_train = np.resize(x_train, (xt, maxlen, 1))
    y_train = np.resize(y_train, (len(x_train), n_class))
    model.fit(x_train, y_train, epochs=25, batch_size=64, verbose=0)

    x_test = np.resize(x_test, (len(x_test), maxlen, 1))
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
    acc = (tp + tn) / (tp + fn + tn + fp)
    tnr = tn / (tn + fp)
    tpr = tp / (tp + fn)
    ACC.append(acc*100)
    TPR.append(tpr*100)
    TNR.append(tnr*100)
    return ACC, TPR, TNR

