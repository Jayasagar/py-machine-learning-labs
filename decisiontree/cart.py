import csv
from itertools import groupby

class Cart:
    def __init__(self):
        print(self)

    def getTrainingDataset(self):
        trainingDataset = []
        with open('trainingset.csv', 'r') as trainingSet:
            reader = csv.reader(trainingSet, delimiter=',')
            for row in reader:
                trainingDataset.append(row)
        return trainingDataset

    def extractOutputClassSet(self, totalTrainingDataset):
        return [i[-1] for i in totalTrainingDataset]

    def giniStart(self, outputDataset):
        groupByClass = [list(g[1]) for g in groupby(sorted(outputDataset, key=len), len)]

        print(groupByClass)



    # Calculate Gini index for the 'Input Attribute/Feature/Candiate'
    # Example: Calculate Gini for Input Attribute = 'Country'
    # Country	    Allowed?
    # Home Country	Yes
    # India	        Yes
    # USA	        Yes
    # India	        Yes
    # Home Country	Yes
    # Home Country	No
    # India	        No
    # India	        Yes
    # USA	        No
    # USA	        Yes
    def giniIndex(self, inputAttributeSplitDataset):
        n_instances = float(sum([len(group) for group in inputAttributeSplitDataset]))
        print(n_instances)


def main():
        cart = Cart()
        # Training Dataset Transform CSV to array
        # Origin,Salary,Married,Age,Allowed
        trainingSet = cart.getTrainingDataset()

        # Get the output class dataset
        outputClassList = cart.extractOutputClassSet(trainingSet)
        print('outputClassList:', outputClassList)

        # Get Gini Start value
        cart.giniStart(outputClassList)

        print(trainingSet)
        cart.giniIndex(['1', '1'])
        #


if __name__ == "__main__": main()