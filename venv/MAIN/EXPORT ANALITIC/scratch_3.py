import pandas as pd

df = pd.DataFrame({'col1':[1.00, 1, 0.5, 1.50]})

df['new'] = df['col1'].map('{0:g}'.format)
#alternative solution
#df['new'] = df['col1'].apply('{0:g}'.format)
print (df)