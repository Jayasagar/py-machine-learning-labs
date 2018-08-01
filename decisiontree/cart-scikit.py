import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing

from sklearn.tree import DecisionTreeClassifier


def main():
    print('Hi')
    trainingDataFrame = pd.read_csv('trainingset.csv')
    trainingDataFrame.info()
    trainingDataFrame.describe()
    print(trainingDataFrame)

    trainSet = trainingDataFrame.drop(['Allowed'], axis = 1)
    print(trainSet)

    numpyMatrix = trainSet.as_matrix()

    le = preprocessing.LabelEncoder()
    for i in range(3):
        numpyMatrix[:,i] = le.fit_transform(numpyMatrix[:,i])
    print(numpyMatrix)

    outputClasses = trainingDataFrame['Allowed']
    print('outputClasses', outputClasses)

    model = DecisionTreeClassifier()
    model.fit(numpyMatrix, outputClasses)

    print('model', model)

    testData = np.array([['Home Country',80000,'No',34]])
    for i in range(3):
        testData[:,i] = le.fit_transform(testData[:,i])

    predictValue = model.predict(testData)
    print('predictValue', predictValue)

if __name__ == "__main__": main()