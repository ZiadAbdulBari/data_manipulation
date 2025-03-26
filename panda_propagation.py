import pandas as pd
from functools import reduce

data = {'id':[8,1,2,None,8,5,9],'score':[8,5,9,None,7,4,None]}
df = pd.DataFrame(data)
# new_df = df.fillna(method='bfill')
na_column = df.columns[df.isna().any()].tolist()
for i in range(0,len(na_column)):
    test = reduce(lambda d, _: d.fillna(d.rolling(3, min_periods=3).mean().shift()), range(df[na_column[i]].isna().sum()), df)
    df[na_column[i]] = test[na_column[i]]

    

print(df)