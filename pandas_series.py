import pandas as pd
from pandas import Series,DataFrame
import numpy as np


object=Series([5,30,25,20])
# print(object.values)
# print(object.index)


'''topic---use numpy array to series'''
data_array=np.array(['a','b','c'])
s=Series(data_array)
# print(s)


revenue_df=pd.read_excel("C:/Users/Admin/Documents/HashAnalyticsProjects/revenue.xlsx")
# print(revenue_df)

# print(revenue_df.columns) #reading column names
# print(revenue_df['Rank'])

'''topic---reindexing '''
cars=Series(['Audi','Vitz','Corolla'], index=[0,4,8])
# print(cars)
ranger=range(13)
# print(ranger)
cars=cars.reindex(ranger, method='ffill')
# print(cars)

#creating new df using randn
df=DataFrame(np.random.randn(25).reshape(5,5),index=['a','b','c','d','e'],columns=['c1','c2','c3','c4','c5'])

#reindex df rows
df_1=df.reindex(['a','b','c','d','e','f'])
# print(df_1)

#reindex columns
df_2=df_1.reindex(columns=['c1','c2','c3','c4','c5','c6'])
# print(df_2)

#using loc(loc for label based indexing) to reindex
df_3=df_2.loc[['a','b','c','d','e','f'],['c1','c2','c3','c4','c5','c6']]
# print(df_3)


'''topic--dropiong entries'''

cars=Series(['Audi','merc','xtrail'], index=['a','b','c'])
cars=cars.drop('a')
# print(cars)

#dropping dataframes rows/columns
car_df=DataFrame(np.arange(9).reshape(3,3),index=['Audi','merc','xtrail'],columns=['revenue','profit','expenses'])
# print(car_df)

car_df=car_df.drop('xtrail',axis=0)
# print(car_df)
car_df=car_df.drop('profit',axis=1)
# print(car_df)


''' Topic--Handling Null values'''

series1=Series(['A','B','C','D',np.nan])

#validation that a null column exists
# print(series1.isnull())
# print(series1.dropna())

dataframe1=DataFrame([[1,2,3],[5,6,np.nan],[7,np.nan,10],[np.nan,np.nan,np.nan]])

# dataframe1.dropna() #drops any row that contain null values

# print(dataframe1.dropna(how='all'))
# print(dataframe1.dropna(axis=1))#drops any column that contains null values
dataframe2=DataFrame([[1,2,3,np.nan],[4,5,6,7],[8,9,np.nan,np.nan],[12,np.nan,np.nan,np.nan]])
# print(dataframe2)



'''sorting and ranking'''

from numpy.random import randn

ser_1=Series([1500,1000,2500],index=['a','c','b'])
#sorting by index
ser_1=ser_1.sort_index()
# print(ser_1)
#sort by values
ser_1=ser_1.sort_values()
# print(ser_1)
#arranged in ascending order
ser_1=ser_1.rank()
# print(ser_1)

ser2=Series(randn(10))
ser2=ser2.sort_values()
# print(ser2.rank())

'''pandas statistics'''

import matplotlib.pyplot as plt 

array1=np.array([[10,np.nan,20],[30,40,np.nan]])
# print(array1)
df_array=DataFrame(array1,index=[1,2],columns=list('ABC'))
# print(df_array)

df_array.sum() #sum along column\
df_array.sum(axis=1)#sum along indexes
df_array.max()# prints out maxvalues
df_array.min()