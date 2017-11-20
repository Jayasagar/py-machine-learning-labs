import csv
from itertools import groupby
import collections
import numpy as np
import pandas as pd

class Cart:
    outputClassValues = ['Yes', 'No']

    def __init__(self):
        print('Init')

    def conv(s):
        try:
            s=float(s)
        except ValueError:
            pass
        return s

    def getTrainingDataset(self):
        trainingDataset = []
        cursor = []
        df = pd.read_csv('trainingset.csv', header=None)
        numpyMatrix = df.as_matrix()
        print('trainingset.csv as NumPy Array using Pandas', numpyMatrix)
        return numpyMatrix

    def extractInputAttributeAndOutputClass(self, totalTrainingDataset, inputAttributeIndex):
        print('inputAttributeIndex', inputAttributeIndex)
        subset = []
        for trainingRow in totalTrainingDataset:
            #print('trainingRow', trainingRow)
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

    # Input Attribute Value('Home Country') Subset = [['Home Country', 'Yes'], ['Home Country', 'Yes'], ['Home Country', 'No']]
    def giniSubsetIndex(self, totalDatasetRecordCount, valueSubset):
        valueSubsetCount = len(valueSubset)
        # Proportion of subset/Dataset
        # Example: Proportion(count(Origin=Home Country) on total dataset/count(Total rows in dataset))
        attributeProportionInTotalDataset = valueSubsetCount/totalDatasetRecordCount

        giniIndexForAttributeIndexValue = 0
        for outputClass in self.outputClassValues:
            # Get the count of matches for each output category
            outputClassCount = sum(x.count(outputClass) for x in valueSubset)
            print('outputClass', outputClass, 'count', outputClassCount)
            outputClassProportionInAttributeValueSet = outputClassCount/valueSubsetCount
            giniIndexForAttributeIndexValue = giniIndexForAttributeIndexValue +  outputClassProportionInAttributeValueSet * outputClassProportionInAttributeValueSet

        # Gini Calculation for specific attribute value subset
        # Proportion(count(Origin=Home Country) on total dataset/count(Total rows in dataset)) * G(Origin=Home Country)
        giniValue = attributeProportionInTotalDataset * (1 - giniIndexForAttributeIndexValue)
        print('GINI Input Attribute Value', giniValue)
        return giniValue

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

        attributeKeyValue = next(iter(attributeDic))
        print('type(key) == str or type(key) == bool', type(attributeKeyValue))
        # Catogirical values, i.e. String and Boolean
        if ((type(attributeKeyValue) is str or type(attributeKeyValue) is bool)):
            for key, value in attributeDic.items():
                giniIndexResult = giniIndexResult + self.giniSubsetIndex(totalRecords, value)
        if (type(attributeKeyValue) is int or type(attributeKeyValue) is float):
            # Sort the list
            #dtype = [('value', float), ('opClass', str)]
            npInputAttributeSplitDataset = np.array(inputAttributeSplitDataset)
            npInputAttributeSplitDataset = npInputAttributeSplitDataset[npInputAttributeSplitDataset[:,0].argsort()]
            print('sorted data', npInputAttributeSplitDataset)

            # Create a new list with median calculation
            npOnlyAttributeValues = npInputAttributeSplitDataset[:,0]
            npOnlyAttributeValues = np.array(npOnlyAttributeValues, dtype=np.int64)
            print('All attribute values', npOnlyAttributeValues)
            npMedianAdjacentValues = (npOnlyAttributeValues[1:] + npOnlyAttributeValues[:-1]) / 2
            print('median', npMedianAdjacentValues)

            # Calculate the gini for each value as a binary classification(LEFT and RIGHT)
            for value in npMedianAdjacentValues:
                print('value', value)
                dict = {'<=': [], '>':[]}

                for inputValue in inputAttributeSplitDataset:
                    if (float(inputValue[0]) <= value):
                        dict.get('<=').append(inputValue)
                    else:
                        dict.get('>').append(inputValue)

                print('dict', dict)
                for key, value in dict.items():
                    giniIndexResult = giniIndexResult + self.giniSubsetIndex(totalRecords, value)

            # Return the best attribute gini index
            print('continuous values')
        return giniIndexResult

    def giniGain(self, giniStart, giniAttributeIndex):
        return giniStart - giniAttributeIndex

def main():
        cart = Cart()
        # Training Dataset Transform CSV to array
        # Origin,Salary,Married,Age,Allowed
        trainingSet = cart.getTrainingDataset()
        #print('trainingSet: ', trainingSet)

        # Get the output class dataset
        outputClassList = cart.extractColumnValuesAtIndex(trainingSet, -1)
        print('extractColumnValuesAtIndex -1:', outputClassList)

        # Get Gini Start value
        giniStartIndex  = cart.giniStart(outputClassList)
        print('gini Start Index', giniStartIndex)

        giniGainDic = {}
        # Get specific input attribute subset along with output class

        for index in range(len(trainingSet[0]) -1):
            print('####################################################   START   ###########################################################')
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
            print('####################################################   END    ###########################################################')

        print('All Gini Gains', giniGainDic)

if __name__ == "__main__": main()