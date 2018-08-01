import csv
from itertools import groupby
import collections
import numpy as np
import pandas as pd
from enum import Enum

class ConditionOperator(Enum):
    EQ:'EQ'
    LTE: 'LTE'
    GTE: 'GTE'

class Node:
    # attributeName: Input Attribute name in dataset
    # conditionValues: Predicate values required to check the match
        ## It could be array in some instances, such as [Married,Single] i.e. condition match could be either one of teh value.
    # condition: Operator to use on predicate expression
    # classLabel: Applicable to the leaf node, this is to produce output results!
    #
    def __init__(self, attribuIndex, attributeName, conditionValues, condition, leftNode, rightNode, classLabel):
        self.attributeName = attributeName
        self.attribuIndex = attribuIndex
        self.conditionValues = conditionValues
        self.condition = condition
        self.leftNode = leftNode
        self.rightNode = rightNode
        self.classLabel = classLabel # Applicable to the leaf node, this is to produce output results!

    def __repr__(self):
        return repr('attributeName: ' + self.attributeName) + repr(' condition: ' + self.condition) + ', conditionValues: ' + repr(self.conditionValues)

class Cart:
    outputClassValues = [1, 0]
    attributeDictionary = {0: 'Origin', 1: 'Salary(Euros)', 2: 'Married', 3: 'Age', 4: 'Allowed'}


    def __init__(self):
        print('Init')

    def conv(s):
        try:
            s=float(s)
        except ValueError:
            pass
        return s

    # read training set data from the CSV format
    def getTrainingDataset(self):
        trainingDataset = []
        cursor = []
        df = pd.read_csv('trainingset.csv')
        print('DF:', df)

        # print('my_dataframe.columns.values.tolist()', list(df))
        numpyMatrix = df.as_matrix()
        #print('at index dataframe:', df[0])
        print('trainingset.csv as NumPy Array using Pandas', numpyMatrix)
        return numpyMatrix

    # Splits the array into two Groups based on the given condition
    def split(self, dataset, condition):
        return [dataset[condition], dataset[~condition]]

    def splitDatasetByMatch(self, dataset, matchIndex, valuesToMatch, condition):
        if (ConditionOperator.EQ == condition):
            splitDataSetForLeftAndRigth = self.split(dataset, dataset[:, matchIndex] == valuesToMatch)
            print('splitDatasetByMatch', splitDataSetForLeftAndRigth)
            return splitDataSetForLeftAndRigth
        if (ConditionOperator.LTE == condition):
            splitDataSetForLeftAndRigth = self.split(dataset, dataset[:, matchIndex] <= valuesToMatch)
            print('splitDatasetByMatch', splitDataSetForLeftAndRigth)
            return splitDataSetForLeftAndRigth
        if (ConditionOperator.GTE == condition):
            splitDataSetForLeftAndRigth = self.split(dataset, dataset[:, matchIndex] > valuesToMatch)
            print('splitDatasetByMatch', splitDataSetForLeftAndRigth)
            return splitDataSetForLeftAndRigth

    # Excludes the complete column values in a given dataset
    def excludeColumnAtIndex(self, dataset, indexToExclude):
        """Exclude the complete specific column values
        from the given dataset. """

        excludeColumnAtIndex = np.delete(dataset, indexToExclude, axis=1)
        print('exclude at:', indexToExclude,  excludeColumnAtIndex)
        return excludeColumnAtIndex

    # Extract two coloumn values from given dataset for given index and last index i.e. outputclass
    def extractInputAttributeAndOutputClass(self, totalTrainingDataset, inputAttributeIndex):
        print('inputAttributeIndex', inputAttributeIndex)
        subset = []
        for trainingRow in totalTrainingDataset:
            #print('trainingRow', trainingRow)
            subset.append([trainingRow[inputAttributeIndex], trainingRow[-1]])
        return subset

    # Extract complete column values as a single array for given index
    def extractColumnValuesAtIndex(self, totalTrainingDataset, index):
        return [i[index] for i in totalTrainingDataset]

    # Group Array by its values.
    # I/P: ['Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes']
    # Group the array by value. Example O/P: [['No', 'No', 'No'], ['Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes']]
    def groupByValue(self, inputArray):
        groupByClass = [list(j) for i, j in groupby(np.sort(inputArray))]

        print('groupByClass', groupByClass)
        return groupByClass

    # Gini start is the Gini value for the given output class dataset.
    # Usually, gini start is calculated on completed possible dataset output values
    def giniStart(self, outputDataset):
        totalRecords = len(outputDataset)
        print('Total Dataset count', totalRecords)
        proportionSum = 0
        for group in self.groupByValue(outputDataset):
            #print('Each Output class group', group)
            proportionSum = proportionSum + len(group)/totalRecords * len(group)/totalRecords

        giniIndex = 1 - proportionSum
        return giniIndex

    #
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

    # As name suggests, this methods , calculates the Gini Value for the SPECIFIC attribute value. See the example below.
    # Input Attribute Value('Home Country') Subset = [['Home Country', 'Yes'], ['Home Country', 'Yes'], ['Home Country', 'No']]
    def giniAttributeSpecificValueIndex(self, totalDatasetRecordCount, valueSubset):
        print('valueSubset', valueSubset)
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
    def giniIndexForAttribute(self, inputAttributeSplitDataset):

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
                giniIndexResult = giniIndexResult + self.giniAttributeSpecificValueIndex(totalRecords, value)
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
                    giniIndexResult = giniIndexResult + self.giniAttributeSpecificValueIndex(totalRecords, value)

            # Return the best attribute gini index
            print('continuous values')
        return giniIndexResult

    def giniGain(self, giniStart, giniAttributeIndex):
        return giniStart - giniAttributeIndex

    def recursive_split(self, node, dataset, attributeDictionary, outputClassList):
        splitLeftAndRightSubDataset = self.splitDatasetByMatch(dataset, node.attribuIndex, node.conditionValues, node.condition)
        if (len(splitLeftAndRightSubDataset[0]) < 2): # Left node becomes teh leaf node
            #node.leftNode = Node(-1, , ['Yes'], 'EQ', None, None, None)
            print('termination')
        # Stopping condition
            ## Dataset length is below the MINIMUM Threshold?
            ## All the records in dataset has same ATTRIBUTE values or CLASS labels
        # Process Dataset to find the BEST attribute to construct LEFT Node
            # Exclude current node attribute column from dataset

        leftDataset = self.excludeColumnAtIndex(splitLeftAndRightSubDataset[0], node.attribuIndex)
        print('leftDataset: recursive_split', leftDataset)
        nodeLeft = self.bestAttributeNode(leftDataset)
        print('nodeLeft', nodeLeft)
            ## recursive_split(LEFTNode, its dataset)
        # Process Dataset to find the BEST attribute to construct RIGHT Node
            ## recursive_split(LEFTNode, its dataset)
        rightDataset = self.excludeColumnAtIndex(splitLeftAndRightSubDataset[1], node.attribuIndex)
        print('rightDataset: recursive_split', rightDataset)
        nodeRight = self.bestAttributeNode(rightDataset)
        print('nodeLeft', nodeRight)

    def bestAttributeNode(self, dataset):

        outputClassList = self.extractColumnValuesAtIndex(dataset, -1)
        print('extractColumnValuesAtIndex -1:', outputClassList)

        # Get Gini Start value
        giniStartIndex  = self.giniStart(outputClassList)
        print('gini Start Index', giniStartIndex)

        giniGainDic = {}
        bestGainIndex = -1
        bestGainValue = -1
        # Get specific input attribute subset along with output class
        for index in range(len(dataset[0]) -1):
            print('####################################################   START   ###########################################################')
            #for index, item in trainingSet[:-1]:
            inputAttributeSubset = self.extractInputAttributeAndOutputClass(dataset, index)
            print('inputAttributeSubset', inputAttributeSubset)

            # Gini Index for Input Attribute candidate 'Origin/Country'
            giniIndexResult = self.giniIndexForAttribute(inputAttributeSubset)
            print('giniIndexResult for attribute at index', index, giniIndexResult)

            # Gini gain for attribute
            giniGain = self.giniGain(giniStartIndex, giniIndexResult)
            if (giniGain > bestGainValue):
                bestGainIndex = index
            print('giniGain for attribute at index', index, giniGain)
            giniGainDic.update({index: giniGain})
            print('####################################################   END    ###########################################################')

        print('All Gini Gains', giniGainDic)
        print('node set', self.extractInputAttributeAndOutputClass(dataset, bestGainIndex))
        node = Node(bestGainIndex, self.attributeDictionary.get(bestGainIndex), ['Yes'], ConditionOperator.EQ, None, None, None)
        print('node', node)

        return node

def main():
        cart = Cart()
        # Training Dataset Transform CSV to array
        # Origin,Salary,Married,Age,Allowed
        trainingSet = cart.getTrainingDataset()

        # Attribute Dictionary
        #attributeDictionary = {v: k for v, k in enumerate(trainingSet[0])}
        #print('attributeDictionary', attributeDictionary)
        #trainingSet = np.delete(trainingSet, 0, 0)
        #print('after delete frist row : trainingSet', trainingSet)

        #print('Exclude Test: ', cart.excludeColumnAtIndex(trainingSet, 1))
        #cart.splitDatasetByMatch(trainingSet, 2, ['Yes'], 'EQ')

        # Get the output class dataset
        outputClassList = cart.extractColumnValuesAtIndex(trainingSet, -1)
        print('extractColumnValuesAtIndex -1:', outputClassList)

        # Get Gini Start value
        giniStartIndex  = cart.giniStart(outputClassList)
        print('gini Start Index', giniStartIndex)

        giniGainDic = {}
        bestGainIndex = -1
        bestGainValue = -1
        # Get specific input attribute subset along with output class
        for index in range(len(trainingSet[0]) -1):
            print('####################################################   START   ###########################################################')
        #for index, item in trainingSet[:-1]:
            inputAttributeSubset = cart.extractInputAttributeAndOutputClass(trainingSet, index)
            print('inputAttributeSubset', inputAttributeSubset)

            # Gini Index for Input Attribute candidate 'Origin/Country'
            giniIndexResult = cart.giniIndexForAttribute(inputAttributeSubset)
            print('giniIndexResult for attribute at index', index, giniIndexResult)

            # Gini gain for attribute
            giniGain = cart.giniGain(giniStartIndex, giniIndexResult)
            if (giniGain > bestGainValue):
                bestGainIndex = index
            print('giniGain for attribute at index', index, giniGain)
            giniGainDic.update({index: giniGain})
            print('####################################################   END    ###########################################################')

        print('All Gini Gains and bestGainIndex', giniGainDic, bestGainIndex)
        print('Root node set', cart.extractInputAttributeAndOutputClass(trainingSet, bestGainIndex))

        ## Find out condition match and values
        conditionMatchValues = 'Yes'
        condition = ''
        inputAttributeSubset = cart.extractInputAttributeAndOutputClass(trainingSet, bestGainIndex)
        if ((type(inputAttributeSubset[0]) is str or type(inputAttributeSubset[0]) is bool)):
            conditionMatchValues = inputAttributeSubset[0]
            condition = ConditionOperator.EQ

        if (type(inputAttributeSubset[0]) is int or type(inputAttributeSubset[0]) is float):
            conditionMatchValues = inputAttributeSubset[0]
            condition = ConditionOperator.LTE

        rooNode = Node(bestGainIndex, cart.attributeDictionary.get(bestGainIndex), conditionMatchValues, condition, None, None, None)
        print('rooNode', rooNode)

        print('####################################################  ROOT NODE END    ###########################################################')
        cart.recursive_split(rooNode, trainingSet, cart.attributeDictionary, outputClassList)





if __name__ == "__main__": main()