import numpy as np

from scipy.stats import pearsonr

from CSVService import CSVService

csv = CSVService()

# Reference: https://machinelearningmastery.com/statistical-hypothesis-tests-in-python-cheat-sheet/

# This section: statistical tests to check if two samples are related.
dataFrame = csv.read_from_csv()

# print(dataFrame.describe)

corr, p = pearsonr(dataFrame['popularity'], dataFrame['vote_count'])

print('pearson corr:', corr, p)