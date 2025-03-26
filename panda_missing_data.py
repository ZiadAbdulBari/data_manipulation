# /*
# Way of handle missing data
# ? removing rows/column
# ? imputation method: Filling missing with constant/mean/mode/median
# ? propagetion: Forward propagation and backward propagation
# ? interpolation: Linear/polynomial
# */

# TASK- Remove the row or column if null value exist more than 49%

import pandas as pd
data = {'id':[1,2,3,None,5],'score':[5,9,None,7,4]}
df = pd.DataFrame(data)
remove_row = df.dropna(axis=1) #If you want to remove column just put axis=1 into dropna function 
print(remove_row)