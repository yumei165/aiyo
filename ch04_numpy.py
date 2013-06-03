#create array
data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1,dtype = np.float64)
data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2, dtype = np.uint64)
arr2.ndim #2
arr2.shape #(2,4)
arr1.dtype #dtype('float64')
arr1.dtype #dtype('uint64')
numeric_strings = np.array(['1.25', '-9.6', '42'], dtype=np.string_)
numeric_strings.astype(float)
numeric_strings.astype(arr1.dtype)
 #other ways to create array: zeros, ones, empty, arange
np.zeros((3,6)) #3 arrays with each element an array of 6 zeros
np.empty((2,3,2)) #elements are not initialized
np.arange(15) #range(15) as an array
 #other functions: asarray, ones_like, zeros_like, empty_like, eye/identity
 
#operations between arrays and scalars
#elementwise by def., for different size array, check ch12 for broadcasting

#slicing and indexing
 #slicing: different from list: created as view->so changes will be relected on original array
arr[0][1]
arr[0,1]
arr2d[:, 1:]

 #boolean indexing: return a copy of data
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = randn(7, 4)
data[names == 'Bob']
  #The boolean array must be of the same length as the axis it’s indexing.
data[names == 'Bob', 2:]
data[-(names == 'Bob')]  #names != 'Bob'
data[data < 0] = 0

#Fancy Indexing: copy the data
arr = np.empty((8, 4))
for i in range(8):
      arr[i] = i
 #give column numbers, will print in given order
arr[[4, 3, 0, 6]]
arr[[-3, -5, -7]]
 #multiple index array
 # more on reshape in Chapter 12
arr = np.arange(32).reshape((8, 4))
arr[[1, 5, 7, 2], [0, 3, 1, 2]] #only 4 elements were extracted([1,0], [5,3], [7,1], [2,2]
arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]] #this will give 16 elements
arr[np.ix_([1, 5, 7, 2], [0, 3, 1, 2])] #or this

#Transposing Arrays and Swapping Axes: view of data
arr.T
np.dot(arr.T, arr) #A^T*A
 #higher dimensional arrays
arr = np.arange(16).reshape((2, 2, 4))
arr.transpose((1, 0, 2)) #accept a tuple of axis numbers to permute the axes
 #.T is a special case of swapaxes
arr.swapaxes(1, 2) #swap 2nd and 3rd axes

#Universal Functions
sqrt,exp,abs,fabs(non-complex no.),exp,log,sign,ceil,floor,rint,isnan,isfinite,isinf,trigonometri-type,logical_not/-: on one array element-wise
add(-,*,/),floor_divide, maximum, fmax(ignore NaN), power,mod, copysign,greater_equal,logical_and: on two arrays
modf: return two arrays: fractional and integeral part of arr elements

#data processing using arrays
 #compute sqrt(x^2+y^2) where x is from arr1, y is from arr2
pt = np.arange(3,5)
points = np.arange(3)
xs,ys = np.meshgrid(pt,points)
res = np.sqrt(xs**2+ys**2)
In [22]: xs
Out[22]: 
array([[3, 4],
       [3, 4],
       [3, 4]])
       
In [23]: ys
Out[23]: 
array([[0, 0],
       [1, 1],
       [2, 2]])

In [25]: z = np.sqrt(xs**2+ys**2); z
Out[25]: 
array([[ 3.        ,  4.        ],
       [ 3.16227766,  4.12310563],
       [ 3.60555128,  4.47213595]])

import matplotlib.pyplot as plt
plt.imshow(z, cmap=plt.cm.gray); plt.colorbar()
plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")

 #Conditional Logic as Array Operations: np.where
xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])
result = np.where(cond, xarr, yarr) #one or two of arrs can be scalar
arr = randn(4,4)
np.where(arr > 0, 2, arr) #set postive elements as 2
res = np.where(cond1 & cond2, 0, 
        np.where(cond1, 1, 
          np.where(cond2, 2, 3))) #four cases
  #alternative
  res = 3 -1*cond1 - 2*cond2 
  
#math and statistical methods
 #aggregate type: sum, mean, std, var, min/max, argmin/argmax
arr.mean()/np.mean(arr)
arr.sum(0) #optional axis to compute over
 #non-aggregate type: cumsum, cumprod
arr.cumprod(1) #cummulated product over columns

#Methods for Boolean Arrays
 #boolean values are coerced to 1/0
(arr > 0).sum() # Number of positive values
 #any, all: any checks if there is any true, all check if all are true
arr.any()

#sorting, more on chap12 and in pandas
arr.sort(1) #sort by columns(so each row is in sorted order)

#Unique and Other Set Logic
np.unique(names) #return unique names in sorted order
 #in pure python, it would be:
sorted(set(names))
 #check if elements in arr1 in arr2
np.in1d([3,4],[3])
 #other functions: 1d means multi-dim arrays arguments will be treated as 1d array
intersect1d, union1d, setdiff1d(elements in x but not in y), setxor1d(elements in x/y but not in both)

#file input/output
 #binary files
np.save('some_arr', arr) #some_arr.npy will be saved in current dir
np.load('some_arr.npy')
 #multi-dim array
np.savez('2Darr.npz', a=arr, b=arr)
arc = np.load('2Darr.npz')
arc['b']
  #txt files, more details on np.genfromtxt() in ch12
arr = np.loadtxt('array_ex.txt', delimiter=',')

#linear algebra: numpy.linalg
from numpy.linalg import inv, qr
inv,trace,det,eig,qr,svd,pinv,solve(X,b),lstsq(least square solution of Xy=b)
diag(arr): if arr 1D array, return matrix with diagonal arr; if arr matrix, return diagonal as 1D array  

#random in numpy
seed: Seed the random number generator
permutation: Return a random permutation of a sequence, or return a permuted range
shuffle: Randomly permute a sequence in place
rand: Draw samples from a uniform distribution
randint: Draw random integers from a given low-to-high range
randn: Draw samples from a normal distribution with mean 0 and standard deviation 1 (MATLAB-like interface)
binomial: Draw samples a binomial distribution
normal: Draw samples from a normal (Gaussian) distribution
beta: Draw samples from a beta distribution
chisquare: Draw samples from a chi-square distribution
gamma: Draw samples from a gamma distribution
uniform: Draw samples from a uniform [0, 1) distribution
 #example function argmax(1)
arr.argmax(1): the first index to achieve the maximum of arr for each row.








