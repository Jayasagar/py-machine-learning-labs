import numpy as np

from scipy.stats import pearsonr

from CSVService import CSVService

csv = CSVService()

# This section: statistical tests to check if two samples are related.
dataFrame = csv.read_from_csv()

# print(dataFrame.describe)

corr, p = pearsonr(dataFrame['popularity'], dataFrame['vote_count'])

print('pearson corr:', corr, p)