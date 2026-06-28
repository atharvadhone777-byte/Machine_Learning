#Numpy - Numerical Python
import numpy as np
print(np.__version__) #Prints current version

#1. Numpy array - faster than list but contains only same datatype
arr=np.array([1,2,3])     #Declaration of array
print(type(arr))    #<class 'numpy.ndarray'>

arr=arr*2   #Each element gets doubled - 2,4,6

#2. Multidimentional array
arr=np.array('A')
print(arr.ndim)  #It prints 0 because no [] is used

arr=np.array([[1,2,3],
             [4,5,6],
             [7,8,9]])
print(arr.ndim)  #It prints 2 - number of cosecutive '[['
print(arr.shape) #It prints (3,2) i.e number of rows and columns

#Array methods
a=np.array([[1.0,2.0],[2.2,2.3],[2.1,4.3]])
print(a.ndim)   #Prints dimension of array
print(a.itemsize)   #Gives each items size as array is of only same datatype
print(a.dtype)      #Gives datatype of each element
print(a.size)   #Gives size of array
print(a.shape)  #Gives dimensions of (3,2) i.e, 3 rows and 2 columns
b=np.array([[1,2],[2,2],[2,4]], dtype=np.float64)    #It changes datatype to float numbers from integers
a.reshape(2,3)  #It has 2 rows and 3 columns as 2×3 is equal to 3×2 (Compitable)
a.ravel()   #This will convert copy of array in single row, does not change the original array
np.zeros((3,4))    #Creates an array of all zeroes(But speelong zeros rakhna) in 3×4 
np.ones((3,4))  #Creates array of 3×4 of 1
np.linspace(1,5,10) #It generates 10 number inclusive 1 and 5 which are lineraly spaced
ab=np.arange(1,5,2) #It starts from 1 and adds with difference of 2 and ends as we reach or exceeds 5
print(a.min()) #Prints the minimum element
print(a.max()) #Prints the maximum element
print(a.sum())  #Prints sum of all elements
print(a.sum(axis=0))    #Prints the sum in y axis i.e sumof all columns in single row table=1×n
print(a.sum(axis=1))    #Prints the sum of all rows and form a single columns table=n×1
np.sqrt(a)  #Sabhi elements ka square root ho jayga
print(a.dot(b)) #This will do matrix multiplication if compatible

#3. Slicing
#arr[start : end : step]  - row selection
print(arr[0][1])  #First row ka second index #Method = chain indexing
print(arr[0:2])   #Prints all rows excluding roe with index 2
print(arr[::2])   #Prints rows whose index are divisible by 2
print(arr[::-1])  #Prints all rows in reverse
print(arr[::-2])  #Prints rows in reverse order whose reversed index is divisible by 2

#arr[x:y:z, start,end,step] - column selection
print(arr[:,1])  #Selects only column elements wit index 1
print(arr[:,0:2]) #Prints elements of column 0 to 1 excluding 2
print(arr[:,::2]) #Only column elements with index divisible by 2
print(arr[0:2,0:2]) #We selected a quadrant by using both row and column selection

for cell in a.flat: #n2.flat se hum kisi bhi array ko as one dimension use kr skte hai
    print(cell)     #Each element will be printed

print(np.vstack((a,b)))    #This will concatenate two arrays vertically - should have same number of columns
print(np.hstack((a,b)))     #This will concatinate horizontally - should have same number of rows
result3 = np.hsplit(a,3)      #This splits array horizontally |--|--|--| aise #Here result3 will become an array of 3 arrays
result3=np.vsplit(a,3)      #Vertically split karega upar wale se ulta kaam

#4. Arithmetic
#Scalar arithmetic
#Each element gets changed according to opeartion
arr+1
arr-1
arr*3
arr/4
arr**4

#Vectorized math functions
np.sqrt(arr)
np.round(arr)
np.ceil(arr)
np.floor(arr)
print(np.pi) #Gives pi value 3.1415
print(np.pi*arr**2)  #If values of arr are radii then this prints area of that circles

#Element wise arithmetic - Corresponding elemnts gets changed accoringly
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])

arrx=arr1+arr2
arrx=arr1-arr2
arrx=arr1*arr2
arrx=arr1/arr2


#5. Broadcasting
# Broadcasting allows NumPy to perform operations on arrays with different shapes by virtually expanding dimensions so they match larger arrays shape

#The dimensions have same size or One of the dimensions has a size of 1
arr1=np.array([[1,2,3,4,5,6,7,8,9,10]])
arr2=np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
print(arr1*arr2) #Prints tables from 1 to 10
#To be compatible either the number of rows and columns must be equal or any of them would be 1
#(4,1) and (4,4) is compatible


#6. Aggregate functions
x=np.sum(arr)
x=np.mean(arr)
x=np.std(arr)   #std - standard deviation = measure of spread of data
x=np.var(arr)   #Variance - Square of standar deviation
x=np.min(arr)
x=np.max(arr)
x=np.argmin(arr)    #Gives position of minimum element
x=np.argmax(arr)
x=np.sum(arr,axis=0) #Sum of all elements in each columns ka ek array dega
x=np.sum(arr,axis=1) #Sum of all elements in each row ka ek array dega

#7. Filtering - Refers to the process of selecting elements from an array that match given condition

new_arr=arr[((arr>=3) & (arr<100)) | (arr%2==0)] 
#Only those elements which satisfies condition with '&b and '|' also, but this method will not preserve the shape

#'where' method
# np.where(condition, Array name, Elements which does not satisfy get replaced with this number)
new_arr=np.where(arr>=3, arr, 0)
print(new_arr)  #Shape retained as not required elements are set to zero but they are still at there place

#8. Random numbers
rng=np.random.default_rng(seed=1)
print(rng.integers(low=1,high=7,size=(1,2)))  #Gives 4 random numbers between 1 and 6 excluding 7 in (1,2) matrix
#If seed is set to any non-zero number then it will always give same output

#To get float numbers instead of integers
print(np.random.uniform(low=-1,high=1,size=1)) #Gives a float number between -1 and 1

#To shuffle an array
rng=np.random.default_rng()
rng.shuffle(arr)  #Array got shuffled

#To get any random element of array
x=rng.choice(arr,size=2)
print(x)  #Gives any 2 random element

#9. Numpy array takes less size than list
import sys
l=range(1000)   #This created a list with 1000 integers 0 to 999
print(sys.getsize(5)*len(l))    #Python list will be taking 14000 bytes

array = np.arange(1000) #This creates array of elements 0 to 999 i.e, of size 1000
print(array.size*array.itemsize)   #array.size is total length of array , array.itemsize is size of an item in the array #numpy array is taking 4000 bytes so it is better

#10. numpy is faster
l1=range(1000)
l2=range(1000)
a1=np.arange(1000)
a2=np.arange(1000)
import time
start1 = time.time() #Marks the current time in microseconds
result=[(x+y) for x,y in zip(l1,l2)]    #It will add first element of l1 list and first element of l2 list and store in result list
print(time.time()-start1*1000)   #This prints the time difference i.e time taken to execute this program

start2=time.time()
result2=a1+a2   #Adds corresponding elements of both arrays
print(time.time()-start2*1000)  #This shows numpy takes 10times less time than python list

#11. Printing of numpy array

n2=[[1,2],[2,3],[3,4]]
for y in n2.flatten():      #Instead of printing a row at a time it is printing a single elements row by row
    print(y)                #Ans - 1 2 2 3 3 4

for x in np.nditer(n2,order='C'):    #order='C' will have same effect as flatten shown above
    print(x)                        #Ans - 1 2 2 3 3 4

for x in np.nditer(n2,order='F'):    #order='F' will print each element first of column 1 then column 2 and accordingly
    print(x)                        #Ans - 1 2 3 2 3 4

for x in np.nditer(n2,order='F',flags=['external_loop']):   #This will print column 1 then column 2 but each column inside []
    print(x) 

for x in np.nditer(n2,op_flags=['readwrite']):              
    x[...]=x*x              #Original array gets modified and each elements square gets stores originally in that array using ...


