from scipy.stats import ttest_ind

from CSVService import CSVService

csv = CSVService()

dataFrame = csv.read_from_csv()

stat, p = ttest_ind(dataFrame['vote_count'], dataFrame['vote_average'])

print('Stat:', stat, "p:", p)
