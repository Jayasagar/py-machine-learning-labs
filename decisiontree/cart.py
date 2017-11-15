import csv
from itertools import groupby

class Cart:
    def __init__(self):
        print('Init')

    def getTrainingDataset(self):
        trainingDataset = []
        with open('trainingset.csv', 'r') as trainingSet:
            reader = csv.reader(trainingSet, delimiter=',')
            for row in reader:
                trainingDataset.append(row)
        return trainingDataset

    def extractColumnValuesAtIndex(self, totalTrainingDataset, index):
        return [i[index] for i in totalTrainingDataset]

    def groupByValue(self, inputArray):
        # Group the array by value. Example: [['No', 'No', 'No'], ['Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes']]
        groupByClass = [list(g[1]) for g in groupby(sorted(inputArray, key=len), len)]

        print('groupByClass', groupByClass)
        return groupByClass

    def giniStart(self, outputDataset):
        totalRecords = len(outputDataset)

        proportionSum = 0
        for group in self.groupByValue(outputDataset):
            print('Each Output class group', group)
            proportionSum = proportionSum + len(group)/totalRecords * len(group)/totalRecords

        giniIndex = 1 - proportionSum
        return giniIndex


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
        # Total rows of the given dataset
        totalRecords = len(inputAttributeSplitDataset)

        # Group list by Output class. i.e. by 'no' and 'yes' groups
        groupByClass = [list(g[1]) for g in groupby(sorted(inputAttributeSplitDataset, key=len), len)]
        #inputAttributeValueList = self.extractColumnValuesAtIndex(inputAttributeSplitDataset, 0)
        print('inputAttributeValueList 0:', groupByClass)

        print('')


def main():
        cart = Cart()
        # Training Dataset Transform CSV to array
        # Origin,Salary,Married,Age,Allowed
        trainingSet = cart.getTrainingDataset()
        print('trainingSet: ', trainingSet)

        # Get the output class dataset
        outputClassList = cart.extractColumnValuesAtIndex(trainingSet, -1)
        print('extractColumnValuesAtIndex -1:', outputClassList)

        # Get Gini Start value
        giniStartIndex  = cart.giniStart(outputClassList)
        print('gini Start Index', giniStartIndex)

        # Gini Index for Input Attribute candidate 'Origin/Country'
        cart.giniIndex(['1', '1'])

        #


if __name__ == "__main__": main()