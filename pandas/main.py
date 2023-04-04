import pandas as pd
import numpy as np

# my_series = pd.Series([10,27,32,41,5])

# print(my_series.size)
# print(my_series.ndim)
# print(my_series.head(2))
# print(my_series.tail(2))

# **********************************************

# numbers = [[1,2,39,67,90],[1,2,39,67,90]]
# df = pd.DataFrame(numbers)
# print(df)

# **********************************************

arr = np.array([[1,2,39,67,90],[8,12,45,12,8],[2,8,34,90,102]])
df = pd.DataFrame(arr)
print(df.describe().T)