from scipy.stats import ttest_ind
from scipy.stats import ttest_rel
from scipy.stats import f_oneway

from CSVService import CSVService

csv = CSVService()

dataFrame = csv.read_from_csv()

# Tests whether the means of two INDEPENDENT samples are significantly different
stat, p = ttest_ind(dataFrame['vote_count'], dataFrame['vote_average'])

print('Stat:', stat, "p:", p)

# Tests whether the means of two PAIRED samples are significantly different.
stat_1, p_1 = ttest_rel(dataFrame['vote_count'], dataFrame['vote_average'])

print('Paired Student test: ', stat_1, p_1)
    
# Analysis of Variance Test (ANOVA)
stat_2, p_2 = f_oneway(dataFrame['vote_count'], dataFrame['vote_average'])

print('Analysis of Variance Test (ANOVA): ', stat_2, p_2)