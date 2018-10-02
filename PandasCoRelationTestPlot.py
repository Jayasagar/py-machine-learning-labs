import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot

from scipy.stats import pearsonr

from CSVService import CSVService

csv_service = CSVService()

dataframe = csv_service.read_from_csv()
numpy_dataset = dataframe.values

corr, p = pearsonr(numpy_dataset[0], numpy_dataset[1])

print('pearson corr:', corr, p)

# Numpy way of gettign co relation matrix
# co_output = np.corrcoef(numpy_dataset)
# print(co_output)

# Pandas way of getting co-relation matrix
# co_output_df = dataframe.corr()
# print(co_output_df)

first_few_features = dataframe.iloc[:6, :6]
# print(first_few_features) 
co_output_df = first_few_features.corr()
print(co_output_df)

imag_plot = pd.plotting.scatter_matrix(first_few_features, figsize=(20, 20))
pyplot.show()
