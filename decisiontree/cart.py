import csv
from itertools import groupby
import collections

class Cart:
    outputClassValues = ['Yes', 'No']

    def __init__(self):
        print('Init')

    def getTrainingDataset(self):
        trainingDataset = []
        with open('trainingset.csv', 'r') as trainingSet:
            reader = csv.reader(trainingSet, delimiter=',')
            for row in reader:
                trainingDataset.append(row)
        return trainingDataset

    def extractInputAttributeAndOutputClass(self, totalTrainingDataset, inputAttributeIndex):
        print('inputAttributeIndex', inputAttributeIndex)
        subset = []
        for trainingRow in totalTrainingDataset:
            print('trainingRow', trainingRow)
            subset.append([trainingRow[inputAttributeIndex], trainingRow[-1]])
        return subset

    def extractColumnValuesAtIndex(self, totalTrainingDataset, index):
        return [i[index] for i in totalTrainingDataset]

    def groupByValue(self, inputArray):
        # I/P: ['Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes']
        # Group the array by value. Example O/P: [['No', 'No', 'No'], ['Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes']]
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

    def attributeDic(self, inputAttributeSplitDataset):
        attributeDic ={}
        for row in inputAttributeSplitDataset:
            if row[0] in attributeDic:
                # append the new number to the existing array at this slot
                attributeDic[row[0]].append(row)
            else:
                # create a new array in this slot
                attributeDic[row[0]] = [row]

        print('attributeDic', attributeDic)
        return attributeDic

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

        giniIndexResult = 0

        # Total rows of the given dataset
        totalRecords = len(inputAttributeSplitDataset)

        # Transform to dictionary by 'Input Attribute Value'
        attributeDic = self.attributeDic(inputAttributeSplitDataset)

        for key, value in attributeDic.items():
            print('value', value)
            attributeCount = len(value)
            # Example: Proportion(count(Origin=Home Country) on total dataset/count(Total rows in dataset))
            attributeProportionInTotalDataset = attributeCount/totalRecords

            giniIndexForAttributeIndexValue = 0
            for outputClass in self.outputClassValues:
                outputClassCount = sum(x.count(outputClass) for x in value)
                print('attribute', key, 'outputClass', outputClass, 'count', outputClassCount)
                outputClassProportionInAttributeValueSet = outputClassCount/attributeCount
                giniIndexForAttributeIndexValue = giniIndexForAttributeIndexValue +  outputClassProportionInAttributeValueSet * outputClassProportionInAttributeValueSet

            giniIndexResult = giniIndexResult + attributeProportionInTotalDataset * (1 - giniIndexForAttributeIndexValue)

        return giniIndexResult

    def giniGain(self, giniStart, giniAttributeIndex):
        return giniStart - giniAttributeIndex

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

        giniGainDic = {}
        # Get specific input attribute subset along with output class

        for index in range(len(trainingSet[0]) -1):
        #for index, item in trainingSet[:-1]:
            inputAttributeSubset = cart.extractInputAttributeAndOutputClass(trainingSet, index)
            print('inputAttributeSubset', inputAttributeSubset)

            # Gini Index for Input Attribute candidate 'Origin/Country'
            giniIndexResult = cart.giniIndex(inputAttributeSubset)
            print('giniIndexResult for attribute at index', index, giniIndexResult)

            # Gini gain for attribute
            giniGain = cart.giniGain(giniStartIndex, giniIndexResult)
            print('giniGain for attribute at index', index, giniGain)
            giniGainDic.update({index: giniGain})

        print('All Gini Gains', giniGainDic)

if __name__ == "__main__": main()