# HASHANALYTICS DATA ANALYSIS INTERNSHIP-Charity Wanjiru #
##ASSIGNMENT 1##
### Numpy Fundamentals and Pandas###

Installations needed

- numpy
- pandas

The first step after installing the needed packages, Create new project and inside the project create new file where all the code goes.
Then import the packages you will need. For example `import numpy as np`

####  ARRAYS IN NUMPY ####
An array in numpy is similar to a python list. e.g  this is a list of  integers `x=[1,2,3,4]`. There are different types of arrays such as **one dimension arrays** `my_list=[1,2,3,4] my_array=np.array(my_list)`, **two dimension arrays** `my_list2=[5,6,7,8] my2d_array=np.array([my_list,my_list2])`.

In instances where you want to check how many rows and columns your array contains.use the `.shape` function like so `print(my2d_array.shape)`.
To find out the data type that your array contains `print(my_array.dtype)`.

####Using Other Numpy Functions to create arrays####
using **zero**,**ones**,**eye**, **empty**,**arange**,**exponential**,**sqrt**,**add**,**random**,**Maximum**

    zero_array=np.zeros(5) #creates a new array with(1-5)all elements are zero

    ones_array=np.ones([5,5]) #get all elements as 1(5rows/5columns)

    empty_array=np.empty(5)#creates randoms values from memory
    
    eye_array=np.eye(3,3)#n*n matrix with ones and zeros
    
    arange_array=np.arange(5,50,2)#create array with specified sequence

    expo=np.exp(arange_array) #using exponetial function

    sqrt_func=np.sqrt(arange_array) #using the sqrt function

    added=np.add(array1,array1) #using add funct to add two arrays

    maxed=np.maximum(added,array1)#using maximum function

    
    

    


####scalar operations on array####
scalar operations allow you to treat items of an array the same while dealing with it as arrays

    array1=np.array([[1,2,3,4],[5,6,7,8]]) #two dimension array


**scalar multiplication**

    array2=array1*array1 #each number multiplies with each number in the array

**exponetial multiplication**

    array3=array1**3#Raise each number to the 3rd power


 **Scalar subtraction**

    array4=array1-array1 #each number gets subtracted by itself

**Reciprocal**

    print(1/array1) #each number has a reciprocal of 1

####access members of array using array index####

    arr=np.arange(0,12)# give the range between 0-11
    arr[0:4]=20 #assigns 20 to values 0-4 
    arr2d[:2,1:]=15 # assigns 15 to values

#####index in two dimension array#####
    arr2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
    print(arr2d[0])#prints out 1st row
    print(arr2d[1])#prints out 2nd row
    print(arr2d[2])#prints out 3rd row

#####accessing each column#####
     print(arr2d[0][2])

#####array slicing#####
    slice1=arr2d[0:2,0:2]

#####using loops to index#####
   
    for i in range(arr_len):
    	arr2d[i]=i

When you would like to reuse your array without having the recent changes reflect in it. Use

    arr2=arr.copy() #command to allocate extra memory while making changes


####saving Numpy arrays####

The first step have an array

    single_array=np.arange(50)
Then use the `.save` function then add the desired array  name`'saved_single_array'` then include the array you want to save `single_array`

     np.save('saved_single_array',single_array)#saving a single array
To read the array saved. use `.load` and add `.npy ` to desired array name `'saved_single_array.npy'`

    load_array=np.load('saved_single_array.npy')#reading a single array

####saving multiple arrays in computer memory####
Then use the `.savez` function then add the desired array  name`'saved_multiple_array'` then assign `x` and `y` to the arrays you want to save respectively

    np.savez('saved_multiple_array',x=single_array,y=array1)
To read the array saved. use `.load` and add `.npz ` to desired array name `'saved_multiple_array.npz'`
    load_multiple_array=np.load('saved_multiple_array.npz')

To print out each array separately, use `[x]` or `[y]`

    print(load_multiple_array['y'])

###STATISTICAL AND MATHEMATICAL PROCESSING OF ARRAYS###

 `axes_values=np.arange(-100,100,10)`

**using meshgrid to plot graphs**

    dx,dy=np.meshgrid(axes_values,axes_values)
    function=2*(dx)+3*(dy)
    


**ploting with matplotlib**

    plt.imshow(function)# show graph for fuction
    plt.title('function of plot 2*(dx)+3*(dy)') # title of graph function
    plt.colorbar()#color key
    plt.savefig('myfig.png')# save your image
###USING WHERE###
    
To check whether a condition is true, one can use `.where`

    y=np.array([10,15,20,25])
    z3=np.where(y>0,0,1) 

# PANDAS  

To get started you need to `import pandas as pd` then  `from pandas import series,dataframe`
####series####
    
    object=Series([5,30,25,20])   
series in pandas is one-dimensional array that can hold different data types.Pandas Series is equivalent to a column.

**To convert numpy array to a series**

    data_array=np.array(['a','b','c'])
    s=Series(data_array)

   
 **Reading data from different file types**

    revenue_df=pd.read_excel("revenue.xlsx") #reading excel files
    revenue_df=pd.read_csv("revenue.csv") #reading csv files
    revenue_df=pd.read_clipboard() #reading clipboard copied content
**Reading column names**

    print(revenue_df.columns) #reading column names
**Accessing  specific column using column name**

    print(revenue_df['Rank']) 
**Accessing  specific column using column index**

 `print(revenue_df[[0:2]) #returns 3 columns`

**Re-indexing in pandas**

    cars=Series(['Audi','Vitz','Corolla'], index=[0,4,8])
    
    ranger=range(13)
    
    cars=cars.reindex(ranger, method='ffill') #using the ffill function
**Using `randn `to create a dataframe**

    df=DataFrame(np.random.randn(16).reshape(2,2),index=['a','b'],columns=['c1','c2'])
**re-indexing  rows**

    df_1=df.reindex(['a','b','c'])
**re-indexing columns**

    df_2=df_1.reindex(columns=['c1','c2','c3'])
**using loc(loc for label based indexing) to reindex**

    df_3=df_2.loc[['a','b','c'],['c1','c2','c3']]
**Dropping entries**

    `cars=Series(['Audi','merc','xtrail'], index=['a','b','c'])
    cars=cars.drop('a')
**dropping dataframes rows/columns**

    car_df=DataFrame(np.arange(9).reshape(3,3),index=['Audi','merc'],columns=['revenue','profit'])
    car_df=car_df.drop('merc',axis=0)#dropping row
    car_df=car_df.drop('profit',axis=1)#dropping columns



