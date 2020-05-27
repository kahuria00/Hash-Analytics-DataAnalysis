import numpy as np
import matplotlib.pyplot as plt


# one dimension array
my_list=[1,2,3,4]
# my_array=np.array(my_list)
# # print(my_array)

#two dimension array
my_list2=[5,6,7,8]
my_array=np.array([my_list,my_list2])
# print(my_array)

#use shape
# print(my_array.shape) #checking how many rows and columns an array has

#finding out the data types of an array's content
# print(my_array.dtype)

#using zero,eye empty,arange
zero_array=np.zeros(5) #creates a new array with(1-5)all elements are zero
# print(zero_array)

ones_array=np.ones([5,5]) #get all elements as 1(5rows/columns)
# print(ones_array)

empty_array=np.empty(5)
# print(empty_array)

eye_array=np.eye(5)# identity array
# print(eye_array)

arange_array=np.arange(5,50,2)
# print(arange_array)

#scalar operations on array
array1=np.array([[1,2,3,4],[5,6,7,8]]) #two dimension array
# print(array1)

#scalar multiplication
array2=array1*array1 #each number multiplies with each number in the array
# print(array2)

#exponetial multiplication
array3=array1**3
# print(array3)

#Scalar subtraction
array4=array1-array1 #each number gets subtracted by itself
# print(array4)


#receprical
# print(1/array1)


#access members of array using array index(one dimension)

arr=np.arange(0,12)# give the range between 0-11
# print(arr)
arr[0:4]=20
arr2=arr.copy() #command to allocate extra memory while making changes
# print(arr2)

#index in two dimension array
arr2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(arr2d)
# print(arr2d[0])#prints out 1st row
# print(arr2d[1])#prints out 2nd row
# print(arr2d[2])#prints out 3rd row

#accessing each column
# print(arr2d[0][2])

#array slicing
slice1=arr2d[0:2,0:2]
# print(slice1)
arr2d_copy=arr2d.copy()

arr2d[:2,1:]=15
# print(arr2d)

#using loops to index
arr_len=arr2d.shape[0]

for i in range(arr_len):
	arr2d[i]=i

# print(arr2d)

#arange ,Exponetial,random addition maximum,sqrt 
arrayed=np.arange(15)#using  a range function
# print(arrayed) 

a_range=np.arange(1,15,2) #using arange function
# print(a_range)

expo=np.exp(arrayed) #using exponetial function
# print('this is exponetial',expo)

sqrt_func=np.sqrt(a_range) #using the sqrt function
# print('this is sqrt',sqrt_func)

added=np.add(array1,array1) #using add funct to add two arrays
# print('this is addition',added)

maxed=np.maximum(added,array1)
# print("this is max",maxed)

#saving Numpy arrays

single_array=np.arange(50)

# np.save('saved_single_array',single_array)

# load_array=np.load('saved_single_array.npy')
# print(load_array)

#saving multiple arrays in comp memory
# np.savez('saved_multiple_array',x=single_array,y=array1)
# load_multiple_array=np.load('saved_multiple_array.npz')
# print(load_multiple_array['y'])

# Statistical and mathimatical processing of arrays

# axes_values=np.arange(-100,100,10)
# dx,dy=np.meshgrid(axes_values,axes_values)

# print('dy',dy)
# print('dx',dx)

# function=2*(dx)+3*(dy)
# function2=np.cos(dx)+np.cos(dy)

# print(function)
'''ploting with matplotlib'''

# plt.imshow(function)
# plt.imshow(function2)
# plt.title('function of plot 2*(dx)+3*(dy)')
# plt.title('function cos plot')
# plt.colorbar()
# plt.savefig('myfig.png')
# plt.savefig('myfig2_cos.png')


#conditional clause and boleean operations
x=np.array([100,400,500,600,])#each member has 'a'
y=np.array([10,15,20,25])#each member has 'b'
condition=np.array([True,True,False,False])#each member has cond

#use loops indirectly
z=[a if cond else b for a,cond,b in zip(x,condition,y)]
# print(z)

#using where
z2=np.where(condition,x,y)
# print(z2)

z3=np.where(x>0,0,1)
# print('z3:',z3)
n=np.array([[1,2,3],[4,5,6]])
# print('sum of n:',n.sum(0))

# print("sum of x",x.sum())# get the sum of all elements inthe array
# print('mean of x:',x.mean()) #get the mean
# print("standard deviation of x:",x.std()) # get the standard deviation
# print('variance of x:',x.var())# variance (square of std)

