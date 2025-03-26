import pandas as pd
data = {'id':[1,2,3,8,5],'score':[5,9,None,7,4]}
df = pd.DataFrame(data)
for col in df.columns:
    if df[col].isnull().any():
        df[col] = df[col].fillna(df[col]).mean()
print(df)