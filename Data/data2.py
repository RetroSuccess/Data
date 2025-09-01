from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_csv("movies_info.csv")

print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print(df.shape)
print(df.columns)