# импорт необходимых библиотек 
import pandas as pd 
#import numpy as np 
import random
 
lst = ['robot'] * 10
#print(f"Первый список: \n", lst)
lst += ['human'] * 10
#print(f"Второй список: \n", lst)
random.shuffle(lst)
#	создание DataFrame
data = pd.DataFrame({'whoAmI': lst})
# вывод результата 
print(data)

#	получение уникальных значений столбца
unique_values = data['whoAmI'].unique()
#	создание нового DataFrame с нулевыми значениями
one_hot_df = pd.DataFrame(0, index=data.index, columns=unique_values)
#	перебор уникальных значений и установка 1 в соответствующий столбец
for value in unique_values:
    one_hot_df.loc[data['whoAmI'] == value, value] = 1 

# вывод результата 
print(one_hot_df)

#задача решена без использования функции get_dummies
