import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot

from statsmodels.graphics.gofplots import qqplot

from CSVService import CSVService

class NormalityFrameowrk:
    def __init__(self):
        self.csv = CSVService()

    def main(self):
        print('Hello')
        dataFrame = self.csv.read_from_csv()

        # print('CSV Read Describe data:', dataFrame)
        # print('Maximum value:', dataFrame.max())
        print('4th Row:', dataFrame.loc[4])

        # Type: Pandas Series
        popularity  = dataFrame['popularity']
        print('Max', type(popularity), popularity.max())

        ### Hsitogram
        # pyplot.hist(popularity)
        # pyplot.show()

        #### QQ Plot
        # qqplot(popularity, line='s')
        # pyplot.show()


        

normality_framework = NormalityFrameowrk()
normality_framework.main()