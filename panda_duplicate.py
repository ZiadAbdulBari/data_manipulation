import pandas as pd
data = {'id':[1,1,2,4,5,5,6], 'score':[10,10,20,60,50,50,40]}
df = pd.DataFrame(data)
detect_duplicate = df[df.duplicated()]
remove_dublidate = df.drop_duplicates()
print(remove_dublidate)