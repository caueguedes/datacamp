import pandas as pd

df = pd.read_csv('HistoricalQuotes.csv')
df.head()
df.tail()

df.describe()
print(df.describe(include='object'))
print(df.describe(include='all'))
print(df.describe(percentile=[.1, .5, .9]))
print(df.describe(exclude=float))

df.plot(x='Date', y='High',
        rot=90, title='Date High plot')
df.plot(x='Date', y='High', kind='bar', title='Bar Plot')

# Plot Types
# line, bar, barh, hist, box, density, area, pie, scatter, hexbin,