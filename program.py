import pandas as pd
import numpy as np
df = pd.read_csv("class.csv")
df.head()
data = df.values
array = np.random.choice(16, 10)
array = np.array(array)
for i in array:
    print(data[i][3])
