import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot

from statsmodels.graphics.gofplots import qqplot
from scipy.stats import normaltest

from scipy.stats import shapiro

from CSVService import CSVService

# reference: https://machinelearningmastery.com/a-gentle-introduction-to-normality-tests-in-python/
class NormalityFrameowrk:
    def __init__(self):
        self.csv = CSVService()

    def main(self):
        print('Hello')
        dataFrame = self.csv.read_from_csv()

        # print('CSV Read Describe data:', dataFrame)
        # print('Maximum value:', dataFrame.max())
        print('4th Row:', dataFrame.loc[4])

        # Type: Pandas Series => transform to Numpy Array
        popularity  = dataFrame['popularity'].values
        print('Max', type(popularity), popularity.max(), popularity.mean(), dataFrame['popularity'].median())

        ### Hsitogram
        # pyplot.hist(popularity)
        # pyplot.show()

        #### QQ Plot
        # qqplot(popularity, line='s')
        # pyplot.show()

        # stat, p = shapiro(popularity)
        stat, p = normaltest(popularity)
        print('Statistics=%.3f, p-value=%.3f', stat, p)
        #Interpret
        alpha = 0.05
        if p > alpha:
            print('Popularity data is in Normal')
        else:
            print('Popularity data in not in Normal ')




normality_framework = NormalityFrameowrk()
normality_framework.main()