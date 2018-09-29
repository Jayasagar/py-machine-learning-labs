from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
import numpy as np

from CSVService import CSVService


class MLModels:
    def __init__(self):
        self.csv_service = CSVService()

    def predict(self, X_validation, Y_validation, algorithm, model):
        # Prediction Report
        predictions = model.predict(X_validation)
        # print('y_validation', Y_validation)
        # print('predictions', predictions)
        print('Accuracy score:', algorithm, accuracy_score(Y_validation, predictions))
        print('Confusion Matrix', confusion_matrix(Y_validation, predictions))
        print('Classification report \n', algorithm, classification_report(Y_validation, predictions))
        return accuracy_score(Y_validation, predictions)
        # return predictions

    def build_cross_validation_result(self, X_train, Y_train, algo, model):
        kfold = model_selection.KFold(n_splits = 10, random_state = 7)
        cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring = 'accuracy')
        # print('cv_results:', cv_results)
        result = "Cross Verification Result -> %s:  %0.4f (+/- %0.4f)" % (algo, cv_results.mean(), cv_results.std()*2)
        print(result)
        return cv_results

    def train_model(self):
        dataframe = self.csv_service.read_from_csv()
        numpy_dataset = dataframe.values

        X = dataframe.iloc[:, 0:5]
        Y = dataframe.loc[:, 'superfan']

        X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size= 0.20)

        print(X_train)

        algorithm_dict = {
            # 'CART': DecisionTreeClassifier(),
            'NB': GaussianNB(),
            # 'SVC': SVC(),
            # 'K-N': KNeighborsClassifier(),
            # 'LR': LogisticRegression(),
            # 'LDA': LinearDiscriminantAnalysis()
        }

        results = {}

        for algo, model in algorithm_dict.items():

            # Model built
            model.fit(X_train, Y_train)

            # Cross Validation Results
            result = self.build_cross_validation_result(X_train, Y_train, algo, model)

            # Predict
            results[algo] = self.predict(X_validation, Y_validation, algo, model)

        print(results)

        # Test for certain data point
        # for algo, model in algorithm_dict.items():
        #     # Model built
        #     model.fit(X_train, Y_train)
        #     unlabelled_data_example = np.array([[0.55, 0.0000000000000000, 0 , 0.34590163934426, 0.700000000000000]])
        #     self.predict(unlabelled_data_example, Y_validation, algo, model)



ml_train_alg = MLModels()
ml_train_alg.train_model()