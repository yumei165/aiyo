from pandas import DataFrame, Series
import pandas as pd

#1, Data Structure

#Series: 1D array-like object, can be used as array in numpy, and as dict
obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
obj.values #array([4,7,-5,3])
obj.index  #array(['d','b','a','c']), can be altered by assignment
obj[['c', 'a', 'd']] # Series with subset index
'b' in obj  #True
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = Series(sdata)  #obj3 will be in sorted order of sdata keys
states = ['California', 'Ohio', 'Oregon', 'Texas']
obj3 = Series(sdata,index = states)

In [25]: obj3
Out[25]:
California NaN
Ohio 35000
Oregon 16000
Texas 71000

pd.isnull(obj3)  #T, F,F,F
obj3.notnull()

  #critical feature: automatically aligns differently indexed data in arithmetic operation
obj3 + obj4  #will do plus for common indices
obj4.index.name = 'state'  #can assign names to object,index

#DataFrame:the data is stored as one or more two-dimensional blocks
  #create dataframe
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
  'year': [2000, 2001, 2002, 2001, 2002],
  'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = DataFrame(data)  #5 rows, 3 columns
DataFrame(data, columns=['year', 'state', 'pop'])  #change the order of columns
  #nonpresent columns will have NaN values
frame2 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'], index=['one', 'two', 'three', 'four', 'five']) 
frame2[['state','year']]  frame2.year   #column retrival, get view of data, use Series.copy() to get a copy
frame2.ix[[0,1]]  #get first and second row
  #modify frame values
val = Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
frame2['debt'] = val
frame2['eastern'] = frame2.state == 'Ohio'
del frame2['eastern']  #delete one column
  #another source: nested dict
pop = {'Nevada': {2001: 2.4, 2002: 2.9},'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame3 = DataFrame(pop)  #in sorted order of key of inner dict
DataFrame(pop, index=[2001, 2002, 2003])  #will match given index from pop
frame3.index.name = 'year'; frame3.columns.name = 'state'; frame3.values; frame3.index(immutable)

#2, Essential functionality
#reindexing: index, fill_value, method, limit, copy(by default true), level
obj = Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'], fill_value = 0)  #if no fill_value provided, will show NaN
  #for time series fill, it's useful to use forward fill method 'ffill'
obj3 = Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
In [85]: obj3.reindex(range(6), method='ffill')
Out[85]:
0 blue
1 blue
2 purple
3 purple
4 yellow
5 yellow

  #for data frame: index and columns can both be reindexed(reindex is not rename!)
frame = DataFrame(np.arange(9).reshape((3, 3)), index=['a', 'c', 'd'], columns=['Ohio', 'Texas', 'California'])
frame.reindex(index=['a', 'b', 'c', 'd'], method='ffill', columns=['Ohio','Utah','California']) #Utah column will be NaN, or use fill_value = n.
  #note: for label reindex, more succinctly to use .ix

#drop entries
  #for series
obj.drop(['b','a'])
  #for dataframe
frame.drop(['a','c']), frame.drop('Ohio', axis = 1)

#indexing, selection, filtering
  #for series
obj[1:4], obj[['b','a','c']] = 5, obj['b':'c'](*this is inclusive*)  #index and selection
obj[obj < 2]
  #for data frame
frame[:2]
frame[frame['Ohio']>3] #selection
frame[frame < 5] = 0 #set value
#selection with ix
frame.ix['a',['Utah','Ohio']] <=> frame.ix['a',[1,0]]
frame.ix[frame.Utah > 3, :1]
frame.ix[2] <=> frame.ix['c']

#3, Arithmetic and data alignment
s1 = Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
s2 = Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])
s1+s2 #'d','f','g' will have value NaN
  #data frame similar. If need fill value:
df1.add(df2, fill_value = 0)  #sub,div,mul

#4, operations
s1-s1[0] #delete first entry.
  #can do frame - series: index of series matches columns of frame





  
  
