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
 #different from list: created as view->so changes will be relected on original array
arr[0][1]
arr[0,1]
arr2d[:, 1:]

 #boolean indexing
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = randn(7, 4)
data[names == 'Bob']
  #The boolean array must be of the same length as the axis it’s indexing.
data[names == 'Bob', 2:]
data[-(names == 'Bob')]  #names != 'Bob'

