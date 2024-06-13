## Задача

Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

## Решение

Я придумала два варианта решения данной задачи + вариант с использованием get_dummies:
 - Решение с помощью цикла - ohe_cycle.py
 - Решение с помощью рекурсии - ohe_recursion.py
 - Решение в одну строку с помощью get_dummies - ohe_get_dummies.py
