import matplotlib.pyplot as plt, pandas as pd

df = pd.read_csv('data.csv', index_col=0) # read csv file
df["Average"] = df["Weight"].mean() # average weight
df.plot() # show graph
plt.show() # show UI