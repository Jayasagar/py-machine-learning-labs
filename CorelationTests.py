import numpy as np

from scipy.stats import pearsonr
from scipy.stats import spearmanr

from CSVService import CSVService

csv = CSVService()

# Reference: https://machinelearningmastery.com/statistical-hypothesis-tests-in-python-cheat-sheet/

# This section: statistical tests to check if two samples are related.
dataFrame = csv.read_from_csv()

# print(dataFrame.describe)

corr, p = pearsonr(dataFrame['vote_count'], dataFrame['vote_average'])

print('pearson corr:', corr, p)


corr1, p1 = spearmanr(dataFrame['vote_count'], dataFrame['vote_average'])

print('Spearman Coreation result:', corr1, p1)