import matplotlib
matplotlib.use('TkAgg')

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

        popularity  = dataFrame['popularity']
        print('Max', type(popularity), popularity.max())

normality_framework = NormalityFrameowrk()
normality_framework.main()