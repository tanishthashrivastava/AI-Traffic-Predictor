import pandas as pd

df = pd.read_csv("data/traffic_data.csv")
print(df.info())
print(df.head())  