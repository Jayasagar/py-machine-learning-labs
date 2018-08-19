import pandas as pd

class CSVService:

    def read_from_csv(self):
        return pd.read_csv('tmdb-movies-final-features.csv')