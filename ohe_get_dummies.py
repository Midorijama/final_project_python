import pandas as pd
import random
              
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
print (data)
print(pd.get_dummies(data, prefix=["I_am"], dtype = int))