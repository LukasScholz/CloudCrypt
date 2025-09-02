import pandas as pd


class Config:

    def __init__(self, config_file):
        self._data = {}
        df = pd.read_csv(config_file, skipinitialspace=True)
        for i, config in enumerate(df["ConfigName"]):
            self._data[config] = df.iloc[i]["ConfigValue"]

    def __getattr__(self, key):
        return self._data[key]
