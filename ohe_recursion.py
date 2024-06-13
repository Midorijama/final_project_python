import pandas as pd
import random


def simulate_ohe_recursion (data, ohe_simulation = []):
    if len(data) == 0:
        return ohe_simulation
    check = data.iloc[0].to_string(header=False, index=False)
    if check == 'human':
        temp = [1,0]
    else:
        temp = [0,1]
    ohe_simulation.append(temp) 
    return (simulate_ohe_recursion(data.iloc[1:]))

          
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
df = pd.DataFrame(simulate_ohe_recursion(data), columns = ['human', 'robot'])
print (data)
print(df)