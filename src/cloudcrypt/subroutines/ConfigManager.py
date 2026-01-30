import pandas as pd


class Config:

    def __init__(self, config_file):
        self._data = {}
        df = pd.read_csv(config_file, sep='\s*=\s*')
        for i, config in enumerate(df["ConfigName"]):
            self._data[config] = df.iloc[i]["ConfigValue"]

    def __getattr__(self, key):
        if self._data[key] == "False":
            return False
        elif self._data[key] == "True":
            return True
        return self._data[key]
