import pandas as pd

class CSVService:

def add_to_csv(self, list):
        print(list)
        pd.DataFrame(list).to_csv('tmdb-movies-final-features.csv', index= False)

    def read_from_csv(self):
        return pd.read_csv('tmdb-movies-final-features.csv')