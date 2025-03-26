import polars as pl
data = {'id':[1,1,2,4,5,5,6], 'score':[10,10,20,60,50,50,40]}
df = pl.DataFrame(data)
detect_dup = df.filter(pl.col("score").is_duplicated())
remove_dublidate = df.unique()

print(remove_dublidate)